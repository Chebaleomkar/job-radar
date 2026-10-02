# Daily funding sweep

Run this once a day. Any agent: "read prompts/funding-sweep.md and do it".

## Before you start
Read `AGENTS.md`, `profile/me.md`, `profile/facts.md`, `playbook/strategy.md`, `playbook/outreach.md` and `leads.md`. If `profile/me.md` is missing, stop and run `SETUP.md`.

## Window
Funding announced in the last 24 hours. If the last `companies/funding-*.md` file is older than yesterday, widen the window to cover the gap and say so.

## Tools (free first)
Exa `web_search_exa` / `web_fetch_exa`, Parallel Search, the built-in web search and fetch, `python tools/freesearch.py`. Firecrawl only if a key page can't be read any other way (max 5 credits per run). Never scrape x.com. One call at a time; on HTTP 429 switch tools.

## Steps
1. **Find** startups that announced funding in the window, in the regions and fields from `profile/me.md`. Use primary sources (company blog, press release, primary news, founder post).
2. **Dedupe** against `leads.md` and every `companies/funding-*.md`. Skip anything already there.
3. **Filter** with `playbook/strategy.md` section 2. Drop failures with a one-line reason.
4. **For each survivor:** sourced round + date, what they build, open roles (open the live careers/ATS page; link each), key person (founder / CTO / eng lead) with profile link, email with confidence (AGENTS.md 4.2), fit verdict against the profile, score (strategy section 5).
5. **For 6+ scores:** full brief to `companies/<name>.md` (AGENTS.md 4.1), an email draft and a LinkedIn/X note per `playbook/outreach.md`. If no fitting role exists but they clearly need the user's skills, write a cold pitch or ask for an internship, as the profile says.
6. **Drafts:** if a Gmail / email MCP is connected, save each email as a **draft** (one call per draft, attach the right resume from the profile). Otherwise put the email text in the output file. Never send.
7. **Write** `companies/funding-<YYYY-MM-DD>.md`:
   - Summary table: company | round, amount, date (source) | what they build | role or "cold" | fit | score | contact (verified/guess) | next action
   - Then the briefs or short notes per company, and the dropped list with reasons.
8. **Update** `leads.md`: add 6+ companies to Active, 4 to 5 to Watchlist.

## Reply to the user (short)
- ⏰ Anything due today or overdue in `leads.md`, first.
- Top picks, one action each (who does it).
- Draft IDs if drafts were created.
- Tool calls used (and Firecrawl credits, if any).

Never send, apply or message anyone. No invented facts. No em or en dashes in drafts.
