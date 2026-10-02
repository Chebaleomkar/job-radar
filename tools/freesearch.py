"""Call the keyless search MCPs that OpenCode uses (Exa and Parallel) directly.

Usage:
  python freesearch.py exa "query"
  python freesearch.py parallel "query"
  python freesearch.py fetch <url>          (Parallel web_fetch)
"""
import json, sys, uuid, urllib.request, urllib.error

EXA = "https://mcp.exa.ai/mcp"
PARALLEL = "https://search.parallel.ai/mcp"
SESSION = uuid.uuid4().hex

def call(url, tool, args, timeout=40):
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                       "params": {"name": tool, "arguments": args}}).encode()
    req = urllib.request.Request(url, body, {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
        "User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        raw = r.read().decode("utf-8", "replace")
    # Streamable HTTP may answer as SSE: take the last data: line.
    if raw.lstrip().startswith("event:") or "\ndata:" in raw:
        raw = [l[5:] for l in raw.splitlines() if l.startswith("data:")][-1]
    d = json.loads(raw)
    if "error" in d:
        raise RuntimeError(d["error"])
    res = d["result"]
    if res.get("isError"):
        raise RuntimeError(res["content"][0]["text"][:300])
    return "\n".join(c.get("text", "") for c in res.get("content", []))

def exa(q, n=8):
    return call(EXA, "web_search_exa", {"query": q, "type": "auto", "numResults": n, "livecrawl": "fallback"})

def parallel(q):
    return call(PARALLEL, "web_search", {"objective": q, "search_queries": [q], "session_id": SESSION})

def fetch(url):
    return call(PARALLEL, "web_fetch", {"urls": [url], "session_id": SESSION})

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    mode, arg = sys.argv[1], " ".join(sys.argv[2:])
    print({"exa": exa, "parallel": parallel, "fetch": fetch}[mode](arg))
