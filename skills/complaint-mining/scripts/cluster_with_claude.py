"""
Cluster a CSV/JSONL of complaint snippets into themes using Claude.

Uses prompt caching on the system prompt + cluster instructions, so iterating
on instruction changes is cheap. The reviews payload is on the user turn.

Setup:
    pip install anthropic
    export ANTHROPIC_API_KEY=...

Usage:
    python cluster_with_claude.py reviews.csv --text-col content --max-rows 500 --out clusters.json
    python cluster_with_claude.py reviews.jsonl --jsonl --text-key text --max-rows 500
"""

import argparse
import csv
import json
import os
import sys

try:
    from anthropic import Anthropic
except ImportError:
    sys.exit("install dep: pip install anthropic")


SYSTEM_PROMPT = """You are a senior product researcher running voice-of-customer analysis for an indie founder. You cluster raw user complaints into actionable product themes.

Output rules:
- Produce 5-12 distinct clusters. Merge near-duplicates.
- Name each cluster in the users' own language (e.g., "i lose my streak from one missed day"), not abstract jargon.
- For each cluster: name, 1-line description, 3-5 verbatim quote excerpts (with original wording, including typos), estimated frequency as % of input reviews, and severity tag.
- Severity tags: "showstopper" (people uninstall), "annoyance" (people stay but complain), "vitamin" (nice-to-have wish).
- Drop clusters that are about price, billing, refunds, or customer support — focus on product clusters.
- Output strictly valid JSON. No prose before or after."""


USER_TEMPLATE = """Here are {n} user complaints (one per line, prefixed with rating).

{reviews}

Cluster them per the rules above. Output JSON with this shape:

{{
  "clusters": [
    {{
      "name": "cluster name in user words",
      "description": "1-line description",
      "frequency_pct": 17,
      "severity": "showstopper|annoyance|vitamin",
      "verbatim_quotes": ["quote 1", "quote 2", "quote 3"]
    }}
  ],
  "total_reviews_input": {n},
  "notes": "any caveats about the data quality"
}}"""


def load_reviews(path: str, jsonl: bool, text_col: str, text_key: str, max_rows: int):
    out = []
    if jsonl:
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                obj = json.loads(line)
                text = obj.get(text_key) or ""
                rating = obj.get("rating") or obj.get("score") or "?"
                if text:
                    out.append((rating, text))
                if len(out) >= max_rows:
                    break
    else:
        with open(path, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                text = row.get(text_col, "") or ""
                rating = row.get("rating") or row.get("score") or "?"
                if text:
                    out.append((rating, text))
                if len(out) >= max_rows:
                    break
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("input", help="CSV or JSONL of complaints")
    p.add_argument("--jsonl", action="store_true", help="Input is JSONL")
    p.add_argument("--text-col", default="content", help="CSV column with review text")
    p.add_argument("--text-key", default="text", help="JSONL key with review text")
    p.add_argument("--max-rows", type=int, default=500)
    p.add_argument("--model", default="claude-sonnet-4-6")
    p.add_argument("--out", default=None)
    args = p.parse_args()

    if not os.getenv("ANTHROPIC_API_KEY"):
        sys.exit("missing env var: ANTHROPIC_API_KEY")

    reviews = load_reviews(args.input, args.jsonl, args.text_col, args.text_key, args.max_rows)
    if not reviews:
        sys.exit("no reviews found in input")

    payload = "\n".join(f"[{r}★] {t.strip()[:500]}" for r, t in reviews)
    user_msg = USER_TEMPLATE.format(n=len(reviews), reviews=payload)

    client = Anthropic()
    resp = client.messages.create(
        model=args.model,
        max_tokens=4096,
        system=[
            {
                "type": "text",
                "text": SYSTEM_PROMPT,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[{"role": "user", "content": user_msg}],
    )

    text = resp.content[0].text.strip()
    # Strip code fences if Claude added them
    if text.startswith("```"):
        text = text.split("```", 2)[1]
        if text.startswith("json"):
            text = text[4:]
        text = text.strip()
        if text.endswith("```"):
            text = text[:-3].strip()

    try:
        parsed = json.loads(text)
    except json.JSONDecodeError as e:
        print(f"failed to parse JSON: {e}", file=sys.stderr)
        print(text)
        sys.exit(2)

    output = json.dumps(parsed, indent=2, ensure_ascii=False)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"wrote clusters to {args.out}", file=sys.stderr)
    else:
        print(output)

    usage = resp.usage
    print(
        f"input tokens: {usage.input_tokens} | output: {usage.output_tokens} | "
        f"cache create: {getattr(usage, 'cache_creation_input_tokens', 0)} | "
        f"cache read: {getattr(usage, 'cache_read_input_tokens', 0)}",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
