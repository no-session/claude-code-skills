"""
Pull recent reviews from the Google Play Store.

Requires the `google-play-scraper` package:
    pip install google-play-scraper

Usage:
    python playstore_reviews.py com.example.app [--lang en] [--country us] [--count 1000] [--min-rating 1] [--max-rating 2]

Find the package name in the Play Store URL: play.google.com/store/apps/details?id=com.example.app
"""

import argparse
import csv
import json
import sys

try:
    from google_play_scraper import Sort, reviews
except ImportError:
    sys.exit("install dep: pip install google-play-scraper")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("package", help="Android package name, e.g., com.spotify.music")
    p.add_argument("--lang", default="en")
    p.add_argument("--country", default="us")
    p.add_argument("--count", type=int, default=1000)
    p.add_argument("--min-rating", type=int, default=1)
    p.add_argument("--max-rating", type=int, default=5)
    p.add_argument("--sort", choices=["newest", "rating", "helpful"], default="newest")
    p.add_argument("--out", default=None)
    args = p.parse_args()

    sort_map = {
        "newest": Sort.NEWEST,
        "rating": Sort.RATING,
        "helpful": Sort.MOST_RELEVANT,
    }

    rows, token = [], None
    while len(rows) < args.count:
        batch, token = reviews(
            args.package,
            lang=args.lang,
            country=args.country,
            sort=sort_map[args.sort],
            count=min(200, args.count - len(rows)),
            continuation_token=token,
        )
        if not batch:
            break
        for r in batch:
            if args.min_rating <= r["score"] <= args.max_rating:
                rows.append({
                    "id": r.get("reviewId"),
                    "user": r.get("userName"),
                    "rating": r.get("score"),
                    "thumbs_up": r.get("thumbsUpCount"),
                    "version": r.get("reviewCreatedVersion"),
                    "at": r.get("at").isoformat() if r.get("at") else None,
                    "content": r.get("content"),
                    "reply_content": r.get("replyContent"),
                    "reply_at": r.get("repliedAt").isoformat() if r.get("repliedAt") else None,
                })
        if not token:
            break

    if args.out:
        with open(args.out, "w", newline="", encoding="utf-8") as f:
            if rows:
                writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
                writer.writeheader()
                writer.writerows(rows)
        print(f"wrote {len(rows)} reviews to {args.out}", file=sys.stderr)
    else:
        for r in rows:
            print(json.dumps(r, ensure_ascii=False))

    print(f"total: {len(rows)} reviews ({args.min_rating}-{args.max_rating} stars, {args.lang}/{args.country})", file=sys.stderr)


if __name__ == "__main__":
    main()
