"""Read public X posts for free via X's embed endpoint (no login, no cookies, no API key).

Usage: python xpost.py <post URL or ID> [more ...]
Prints author, date, likes and full text. Undocumented endpoint: if it breaks, fall back to Parallel web_fetch or Firecrawl.
"""
import json, re, sys, urllib.request

def read(ref):
    tid = re.search(r"(\d{10,})", ref).group(1)
    req = urllib.request.Request(
        f"https://cdn.syndication.twimg.com/tweet-result?id={tid}&token=a",
        headers={"User-Agent": "Mozilla/5.0"})
    d = json.load(urllib.request.urlopen(req, timeout=15))
    u = d.get("user", {})
    return (f"@{u.get('screen_name')} ({u.get('name')}) | {d.get('created_at')} | "
            f"likes {d.get('favorite_count')}\nhttps://x.com/{u.get('screen_name')}/status/{tid}\n"
            f"{d.get('text', '').replace('&amp;', '&')}\n"
            + ("[LONG POST: only the first ~280 chars are free; open the link for the rest]\n"
               if d.get("note_tweet") else ""))

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for ref in sys.argv[1:]:
        try:
            print(read(ref))
        except Exception as e:
            print(f"{ref}: FAILED ({e})\n")
