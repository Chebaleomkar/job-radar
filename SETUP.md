# SETUP.md: first-run setup (written for your coding agent)

**Human:** open your coding agent (Claude Code, OpenCode, Codex, Gemini CLI, Pi or any other) in this folder and say:
> Read SETUP.md and set me up.

You can also paste the repo link into any agent and say the same. The agent walks you through everything below. Plan on about 20 to 30 minutes, most of it spent on your profile.

---

**Agent: follow these steps in order. Rules for the whole setup:**
- Never ask the user to paste an API key or secret into the chat. Tell them where to put it (`.env` or their shell profile) and let them do it themselves. In Claude Code they can run shell commands with `! <command>` so the value stays out of the transcript.
- Check before you change anything. Show the user what you'll write, then write it.
- Skip optional steps the user doesn't want. Everything works with only the free, keyless search tools.
- Never send, apply or message anyone during setup.

## Step 1. Know the user's setup
Ask (one message, short):
1. Which agent are they using right now, and which OS (Windows / macOS / Linux)?
2. Which model are they running it on? (See "Models and cost" below. If they want free, point them there.)

Check prerequisites and tell them what's missing, with the install command for their OS:
- `git`, `python` 3.10+ (`python --version`)
- `node` / `npx` (needed only for Firecrawl)
- `uv` / `uvx` (needed only for Gmail drafts): https://docs.astral.sh/uv/
- Optional: `pip install ddgs` (free DuckDuckGo search fallback), `gh` (GitHub CLI)

## Step 2. Create the private working files
Copy the templates (these copies are gitignored and never leave the machine):
- `profile/TEMPLATE.md` → `profile/me.md`
- `profile/facts.TEMPLATE.md` → `profile/facts.md`
- `leads.template.md` → `leads.md`
- `outreach/watchlist.template.md` → `outreach/watchlist.md`
- `.env.example` → `.env`

## Step 3. Connect the tools
Copy the right config for the user's agent from `config/`:

| Agent | Copy | To | Then |
|---|---|---|---|
| Claude Code | `config/claude-code.mcp.json` | `.mcp.json` | Restart; approve the project servers when asked. CLAUDE.md already imports AGENTS.md |
| OpenCode | `config/opencode.json` | `opencode.json` | Restart. Reads AGENTS.md natively |
| Codex CLI | `config/codex.config.toml` | `.codex/config.toml` (trusted project) or `~/.codex/config.toml` | Restart. Reads AGENTS.md natively |
| Gemini CLI | `config/gemini.settings.json` | `.gemini/settings.json` | Restart. GEMINI.md imports AGENTS.md |
| Pi | `config/pi.mcp.json` | `~/.pi/agent/mcp.json` (Pi's docs advise keeping servers with keys at user level) | Restart. Reads AGENTS.md natively. Trust the project once (or run with `-a`), or the `.pi/prompts` slash commands won't load |
| Anything else | Use the closest config | | If it has no MCP support, use `tools/freesearch.py` and the "No-tools mode" in AGENTS.md |

Then walk through each tool:

**3a. Exa and Parallel Search (required, free, no key).** Both hosted MCPs work without a key, with rate limits. Test: run one search on each ("startups that raised a seed round this week"). If the user later wants higher limits, they can get keys at exa.ai and parallel.ai and add them to `.env` (`EXA_API_KEY`, `PARALLEL_API_KEY`), then add the auth header shown in `config/README.md`.

**3b. Firecrawl (optional, free plan, no card).** For JavaScript-heavy pages the free tools can't read. Free plan: 1,000 credits a month (firecrawl.dev/pricing). The user signs up at firecrawl.dev, copies the key, and puts it in `.env` as `FIRECRAWL_API_KEY` themselves. If they skip it, remove the `firecrawl` block from their config so it doesn't error on start.

**3c. Gmail drafts (optional).** Lets the agent save emails as **drafts** in their Gmail. It uses `workspace-mcp` with `--permissions gmail:drafts`: the agent can read mail and write drafts, and **cannot send**. Guide the user through:
1. Go to console.cloud.google.com, create a project.
2. Enable the Gmail API for that project (APIs & Services → Library → Gmail API → Enable).
3. Set up the OAuth consent screen (External, app name anything) and add their own Gmail as a test user.
4. Create credentials → OAuth client ID → type **Desktop app**.
5. Put the client ID and secret in `.env` as `GOOGLE_OAUTH_CLIENT_ID` and `GOOGLE_OAUTH_CLIENT_SECRET` themselves. Never commit `client_secret.json` or a `.credentials/` folder.
6. Restart the agent. The first Gmail call opens a browser to sign in. Check the signed-in account is theirs (AGENTS.md lesson 1).

If they skip it, remove the `google` block from their config. Emails will be written into `outreach/queue/` for them to paste.

**3d. Optional extras.** `gh auth login` for GitHub research. A memory MCP if they already use one (not required: `leads.md` and `companies/` are the memory).

## Step 4. Build the profile (the most important step)
The whole system is only as good as `profile/me.md` and `profile/facts.md`. These are the agent's grounding: it may only claim what's written there.

1. **Collect sources.** Ask the user for whichever they have: resume PDF (save it in `resume/`), GitHub username, portfolio URL, LinkedIn profile (they can paste the text or use LinkedIn's "Save to PDF"), personal site, notable posts.
2. **Read them** (with `gh` for repos; fetch tools for public pages). Draft the profile sections from what you read.
3. **Interview the user** for what sources can't tell you, a few questions at a time:
   - Target roles in order, the dream role, seniority they can honestly claim.
   - Locations that work, citizenship and visa limits, earliest start date.
   - Pay: minimum and target, and what to say if asked.
   - The "No" list: company types, cultures, domains they won't work in.
   - Their story: 2 to 4 true lines that make them human.
   - Why they left their last job, as one **public line**, and anything **private** that must never be mentioned (NDA clients, the real reason a job ended).
   - Writing preferences and words they hate.
4. **Write `profile/facts.md`** with only verifiable facts: each project's real results with conditions, merged PRs with links, published work. Ask the user to confirm every number. Remove anything they can't back up (old resume metrics are a common trap).
5. Show both files to the user and fix anything they correct.

## Step 5. Test run
1. Run `prompts/research-company.md` on one company the user already knows. Check: a brief appears in `companies/`, every fact has a source, the email uses only facts from `profile/facts.md`.
2. Run `prompts/funding-sweep.md` once. Check: `companies/funding-<today>.md` exists, `leads.md` updated, drafts created (if Gmail is connected) and **nothing sent**.
3. Ask the user what felt off, and adjust their profile or `outreach/watchlist.md`.

## Step 6. Run it daily (optional)
- **Inside the agent:** run `/funding-sweep` and `/x-sweep` each morning (slash commands exist for Claude Code, OpenCode, Gemini CLI and Pi; with Codex, say "read prompts/funding-sweep.md and do it").
- **Unattended:** `schedule/run.sh` (macOS/Linux, cron) or `schedule/run.ps1` (Windows, Task Scheduler). Each file's header has the exact line to schedule it. Headless runs auto-approve tools, so only schedule this after Step 5 worked, and read `logs/` the first few days.

## Step 7. Done
Tell the user:
- Their daily routine: run the two sweeps, read the outputs, send what they like by hand, run `/follow-ups` every few days.
- Everything personal stays in gitignored files. If they fork this repo publicly, their job hunt stays local.

---

## Models and cost
job-radar is free and open source. **The model is yours to bring:** use whatever account or credits you already have. We don't provide credits.

Free or cheap options (limits from the providers' own pages, checked 2026-10-02; they change):
- **Gemini CLI** with a Google account login: 1,000 requests a day.
- **OpenRouter** `:free` models: 20 requests a minute; 50 a day, or 1,000 a day after buying at least $10 of credits once. Works with OpenCode, Pi and others.
- **OpenCode Zen** free models, offered "for a limited time". Some may use your prompts for training, so check before putting personal data in.

Honest note: a sweep is a long run with many tool calls and strict rules. Small free models may skip rules or stumble on tools. If results look sloppy, try a stronger model for the sweeps and keep the free one for small tasks.

Search is free by default (Exa and Parallel keyless, DuckDuckGo via `ddgs`). Firecrawl's free plan is optional.
