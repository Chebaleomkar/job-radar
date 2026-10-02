# Daily X and LinkedIn hiring sweep

Run this once a day. Any agent: "read prompts/x-sweep.md and do it".

## Before you start
Read `AGENTS.md`, `profile/me.md`, `profile/facts.md`, `playbook/outreach.md`, `leads.md` and `outreach/watchlist.md`.

## Safety (hard rules)
Never log in to X or LinkedIn. Never use cookies, browser automation or unofficial logged-in APIs. Never DM, like, follow, reply or connect. Public reads only. The user sends every message by hand.

## Tools (free first, one call at a time)
- Find fresh X posts: Parallel Search `web_search` with `site:x.com` (max ~15 calls per run; on HTTP 429 stop and switch to Exa).
- Read one public post: `python tools/xpost.py <url or id>`.
- LinkedIn posts, companies, people, careers pages: Exa.
- Firecrawl search only as a last resort. Never Firecrawl-scrape x.com.

## Steps
1. Run the saved searches in `outreach/watchlist.md` plus variations of the user's target roles and locations. Focus on the last 72 hours (widen if the last sweep file is older). Watch listed handles by searching their names.
2. Skip anything in `leads.md` or earlier `outreach/queue/*-x-sweep.md`. Skip recruiters and agencies, crypto spam, roles outside the user's role family, levels far above theirs.
3. For each real hit: read the post, identify the company and the poster, **verify the role on the company's careers/ATS page**, check fit honestly (name the gaps), find a verified email if one exists.
4. Write a DM that does exactly what the post asks for (if it says "reply with 2 sentences", write 2 sentences). True facts from `profile/facts.md` only. Include the profile link and post link. If a verified email exists, draft the email too (as a Gmail draft if connected, otherwise in the output file).
5. Save to `outreach/queue/<YYYY-MM-DD>-x-sweep.md`. Add lines to `leads.md`. Create `companies/<name>.md` for strong fits. Add useful new handles and any search pattern that worked to `outreach/watchlist.md`.

## Reply to the user (short)
A table: company | role | fit | DM ready / email ready | links. If nothing good, say so in one line, plus one idea for a better search next time. Tool calls used.

Never send anything.
