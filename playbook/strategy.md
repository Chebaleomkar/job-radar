# Discovery strategy: funding first

**Discovery is mechanical, research is narrow, outreach is personal.** Find companies through observable events, filter hard, and only then research.

Job boards are the fallback, not the plan. A company that raised money last week is hiring, often before a posting exists, and before the flood of applications arrives.

## 1. Anti-hallucination rules (every step)
1. Every fact has a **source URL and the date you saw it**. No source: write `unknown`.
2. Funding and dates come from primary sources: company blog or press release, primary news, the founder's own post. Aggregators (Crunchbase, Tracxn, PitchBook snippets) are hints, marked `(unverified)`.
3. A job is open only if you **opened the live posting today**.
4. Emails are `verified` or `guess` (AGENTS.md 4.2). Nothing in between.
5. When sources disagree, open the primary page and say which one you trusted.

## 2. Hard filters (drop the company if any fails; no deep research on dropped companies)
| Filter | Pass if |
|---|---|
| Company type | Matches `profile/me.md` (e.g. builds its own product) |
| Location | One of the user's locations, remote in their region, or visa sponsorship **stated** |
| Role family | One of the user's target roles |
| Level | The posting's ask is realistic for the user, OR there's no posting (cold pitch), OR it says skills beat years |
| Red flags | Nothing from the profile's "No" list |

## 3. Discovery signals (ranked)

### S1. Recent funding (strongest)
- **Window:** raised ≤ 90 days ago. ≤ 30 days is "hot".
- **How:** search queries like `"raises" seed OR "Series A" <your field> <month year>`, `site:techcrunch.com raises <field>`, regional startup news sites, YC batch pages, investor portfolio news.
- **Record:** company, amount, round, date, lead investor, source URL, careers URL.

### S2. Hiring intent
- **ATS velocity** (public JSON, no key):

| ATS | Endpoint | Posted-date field |
|---|---|---|
| Ashby | `https://api.ashbyhq.com/posting-api/job-board/<board>` | `publishedAt` |
| Greenhouse | `https://boards-api.greenhouse.io/v1/boards/<token>/jobs` | `first_published` |
| Lever | `https://api.lever.co/v0/postings/<company>?mode=json` | `createdAt` (ms epoch) |

  **Spike** = 5+ new jobs in 30 days and 2x the previous 30 days, OR 3+ new roles in the user's family in 30 days. Find the board name from the company's careers page links.
- **Founder hiring posts:** "we're hiring", "DM me", "looking for engineers" in the last 30 days. Quote the post in outreach.
- **Monthly hiring threads:** some investors and operators post a monthly "startups hiring" thread on X. Add them to the watchlist.

### S3. Expansion into the user's markets
A new office or entity in the user's city or region, or a new remote policy for it, within 120 days. Expansion elsewhere doesn't help.

### Enrichment only (not a hiring signal)
- **Product launch (≤ 30 days):** use it as the hook and the idea source for the email.

### Dropped
- **New senior executive:** weak signal for early-career roles, and hard to detect without scraping LinkedIn (against its terms).

## 4. Fit check (evidence, not mind-reading)
- **Stack match:** job posts, engineering blog or GitHub mention the user's stack.
- **Problem match:** can the user point to something they built that is close to this company's engineering problem? If not, skip.

## 5. Scoring (research only companies scoring 6+)
| Evidence | Points |
|---|---|
| Funding ≤ 30 days / ≤ 90 days | 3 / 2 |
| Relevant live role at a feasible level | 3 |
| ATS spike or founder hiring post | 2 |
| Expansion into the user's region | 2 |
| Strong / partial match with the user's proof | 2 / 1 |
| Product launch ≤ 30 days (hook available) | 1 |

- 6+: full brief (AGENTS.md 4.1) and outreach.
- 4 to 5: watchlist row in `leads.md`.
- Under 4: drop.

**Rank by real odds of getting hired, not prestige:** legality (location, visa), experience match, live signal.

## 6. Cadence
| When | What |
|---|---|
| Daily | S1 funding sweep, founder hiring posts |
| Weekly | S2 ATS snapshot of tracked companies |
| Monthly | S3 expansion sweep, monthly hiring threads |
| Every contact | Follow-ups (playbook/outreach.md) |
