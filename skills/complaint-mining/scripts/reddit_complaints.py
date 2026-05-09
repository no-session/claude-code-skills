"""
Search Reddit for complaint posts and comments about a target keyword/app.

Requires the `praw` package and Reddit API credentials:
    pip install praw

Reddit credentials:
1. Go to https://www.reddit.com/prefs/apps → "create app" → script type
2. Set env vars:
       export REDDIT_CLIENT_ID=...
       export REDDIT_CLIENT_SECRET=...
       export REDDIT_USER_AGENT="complaint-mining/1.0 by u/yourusername"

Usage:
    python reddit_complaints.py "notion alternatives" --subreddits notion productivity --limit 100
    python reddit_complaints.py "i hate calm app" --limit 50
"""

import argparse
import csv
import json
import os
import sys

try:
    import praw
except ImportError:
    sys.exit("install dep: pip install praw")


COMPLAINT_KEYWORDS = [
    "hate", "sucks", "alternative", "switching from", "gave up on",
    "frustrating", "annoying", "broken", "doesn't work", "uninstalled",
    "deleted", "cancelled subscription", "wish there was",
]


def is_complaint(text: str) -> bool:
    if not text:
        return False
    lower = text.lower()
    return any(kw in lower for kw in COMPLAINT_KEYWORDS)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("query", help="Search term (e.g., app name)")
    p.add_argument("--subreddits", nargs="+", default=["all"], help="Subreddits to search (default: all)")
    p.add_argument("--limit", type=int, default=100, help="Max posts per subreddit")
    p.add_argument("--time", default="year", choices=["hour", "day", "week", "month", "year", "all"])
    p.add_argument("--include-comments", action="store_true", help="Also pull top comments")
    p.add_argument("--filter-complaints", action="store_true", help="Only keep posts/comments with complaint keywords")
    p.add_argument("--out", default=None)
    args = p.parse_args()

    for var in ("REDDIT_CLIENT_ID", "REDDIT_CLIENT_SECRET", "REDDIT_USER_AGENT"):
        if not os.getenv(var):
            sys.exit(f"missing env var: {var}")

    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT"),
    )
    reddit.read_only = True

    rows = []
    for sub in args.subreddits:
        try:
            subreddit = reddit.subreddit(sub)
            for post in subreddit.search(args.query, time_filter=args.time, limit=args.limit):
                text = (post.title or "") + " " + (post.selftext or "")
                if args.filter_complaints and not is_complaint(text):
                    continue
                rows.append({
                    "kind": "post",
                    "subreddit": str(post.subreddit),
                    "id": post.id,
                    "permalink": f"https://reddit.com{post.permalink}",
                    "author": str(post.author) if post.author else None,
                    "title": post.title,
                    "text": post.selftext,
                    "score": post.score,
                    "num_comments": post.num_comments,
                    "created_utc": post.created_utc,
                })

                if args.include_comments:
                    post.comments.replace_more(limit=0)
                    for c in post.comments.list()[:20]:
                        if args.filter_complaints and not is_complaint(c.body):
                            continue
                        rows.append({
                            "kind": "comment",
                            "subreddit": str(post.subreddit),
                            "id": c.id,
                            "permalink": f"https://reddit.com{c.permalink}",
                            "author": str(c.author) if c.author else None,
                            "title": None,
                            "text": c.body,
                            "score": c.score,
                            "num_comments": None,
                            "created_utc": c.created_utc,
                        })
        except Exception as e:
            print(f"r/{sub}: {e}", file=sys.stderr)

    if args.out:
        with open(args.out, "w", newline="", encoding="utf-8") as f:
            if rows:
                writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
                writer.writeheader()
                writer.writerows(rows)
        print(f"wrote {len(rows)} items to {args.out}", file=sys.stderr)
    else:
        for r in rows:
            print(json.dumps(r, ensure_ascii=False))

    print(f"total: {len(rows)} items across {len(args.subreddits)} sub(s)", file=sys.stderr)


if __name__ == "__main__":
    main()
