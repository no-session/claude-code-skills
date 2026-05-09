"""
Pull comments from a YouTube video (e.g., a competitor's review/tutorial).

Requires the `youtube-comment-downloader` package:
    pip install youtube-comment-downloader

No API key required.

Usage:
    python youtube_comments.py "https://www.youtube.com/watch?v=VIDEO_ID" --limit 500 --out comments.csv
"""

import argparse
import csv
import json
import sys

try:
    from youtube_comment_downloader import YoutubeCommentDownloader, SORT_BY_POPULAR, SORT_BY_RECENT
except ImportError:
    sys.exit("install dep: pip install youtube-comment-downloader")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("url", help="Full YouTube URL or video ID")
    p.add_argument("--limit", type=int, default=500)
    p.add_argument("--sort", choices=["popular", "recent"], default="popular")
    p.add_argument("--out", default=None)
    args = p.parse_args()

    sort = SORT_BY_POPULAR if args.sort == "popular" else SORT_BY_RECENT

    downloader = YoutubeCommentDownloader()
    rows = []
    for c in downloader.get_comments_from_url(args.url, sort_by=sort):
        rows.append({
            "id": c.get("cid"),
            "author": c.get("author"),
            "channel": c.get("channel"),
            "text": c.get("text"),
            "votes": c.get("votes"),
            "replies": c.get("replies"),
            "time": c.get("time"),
            "heart": c.get("heart"),
        })
        if len(rows) >= args.limit:
            break

    if args.out:
        with open(args.out, "w", newline="", encoding="utf-8") as f:
            if rows:
                writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
                writer.writeheader()
                writer.writerows(rows)
        print(f"wrote {len(rows)} comments to {args.out}", file=sys.stderr)
    else:
        for r in rows:
            print(json.dumps(r, ensure_ascii=False))


if __name__ == "__main__":
    main()
