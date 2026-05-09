"""
Pull recent reviews from the Apple App Store via the public RSS feed.

No auth required. Up to ~500 most recent reviews per locale per app.

Usage:
    python appstore_reviews.py <APP_ID> [--locale us] [--max-pages 10] [--min-rating 1] [--max-rating 2]

Find APP_ID in the App Store URL: apps.apple.com/us/app/.../id123456789
"""

import argparse
import csv
import json
import sys
import time
import urllib.request
from urllib.error import HTTPError, URLError


RSS_URL = "https://itunes.apple.com/{locale}/rss/customerreviews/id={app_id}/sortBy=mostRecent/page={page}/json"


def fetch_page(app_id: str, locale: str, page: int):
    url = RSS_URL.format(locale=locale, app_id=app_id, page=page)
    req = urllib.request.Request(url, headers={"User-Agent": "complaint-mining/1.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode("utf-8"))


def parse_entry(entry):
    return {
        "id": entry.get("id", {}).get("label"),
        "author": entry.get("author", {}).get("name", {}).get("label"),
        "author_uri": entry.get("author", {}).get("uri", {}).get("label"),
        "title": entry.get("title", {}).get("label"),
        "content": entry.get("content", {}).get("label"),
        "rating": int(entry.get("im:rating", {}).get("label", 0)),
        "version": entry.get("im:version", {}).get("label"),
        "vote_sum": int(entry.get("im:voteSum", {}).get("label", 0)),
        "vote_count": int(entry.get("im:voteCount", {}).get("label", 0)),
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("app_id", help="Apple app numeric ID")
    p.add_argument("--locale", default="us", help="Locale (us, gb, de, fr, jp, in, br, ...)")
    p.add_argument("--max-pages", type=int, default=10, help="1-10; each page = ~50 reviews")
    p.add_argument("--min-rating", type=int, default=1)
    p.add_argument("--max-rating", type=int, default=5)
    p.add_argument("--out", default=None, help="Output CSV path (default: stdout)")
    args = p.parse_args()

    rows = []
    for page in range(1, min(args.max_pages, 10) + 1):
        try:
            data = fetch_page(args.app_id, args.locale, page)
        except (HTTPError, URLError) as e:
            print(f"page {page}: {e}", file=sys.stderr)
            break

        entries = data.get("feed", {}).get("entry", [])
        # First entry on page 1 is the app metadata, not a review — skip.
        if page == 1 and entries:
            entries = entries[1:]

        if not entries:
            break

        for entry in entries:
            review = parse_entry(entry)
            if args.min_rating <= review["rating"] <= args.max_rating:
                rows.append(review)

        time.sleep(0.5)  # be polite to Apple's RSS

    if args.out:
        with open(args.out, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else [])
            if rows:
                writer.writeheader()
                writer.writerows(rows)
        print(f"wrote {len(rows)} reviews to {args.out}", file=sys.stderr)
    else:
        for r in rows:
            print(json.dumps(r, ensure_ascii=False))

    print(f"total: {len(rows)} reviews ({args.min_rating}-{args.max_rating} stars, locale={args.locale})", file=sys.stderr)


if __name__ == "__main__":
    main()
