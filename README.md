# job-radar

**Your coding agent, turned into a job-search partner.** Every morning it finds startups that just raised money, checks whether they fit you, researches the company and the founders, and drafts a short, specific email for you to send. It never sends anything itself.

Works with any CLI coding agent: **Claude Code, OpenCode, Codex, Gemini CLI, Pi**, or anything that reads `AGENTS.md`.

> I built this for my own job search. People asked for it on X, so here it is. [@omkarchebale](https://x.com/omkarchebale)

## What it does

| Workflow | What you get |
|---|---|
| **Funding sweep** (daily) | Startups funded in the last 24 hours that match your roles, locations and visa limits. Each with a sourced funding line, live open roles, the right person to contact, an email that's verified or clearly marked as a guess, a fit score, and a draft email |
| **X / LinkedIn hiring sweep** (daily) | Founder "we're hiring" posts from the last few days, the role checked on the company's own careers page, and a DM written to match exactly what the post asks for |
| **Research a company** | A full brief: what they build, funding, founders' track records, open roles, open-source entry points, red flags, and a verdict |
| **Follow-ups** | Checks your inbox for replies, then drafts the follow-ups that are due |

Everything lands in plain markdown files: `leads.md` as your tracker, `companies/` for briefs, `outreach/queue/` for drafts.

## Why funding first
A company that raised money last week is about to hire, often before it posts a job, and before hundreds of applications arrive. Job boards are the fallback here, not the plan. See `playbook/strategy.md`.

## Setup: let your agent do it
```bash
git clone https://github.com/Chebaleomkar/job-radar
cd job-radar
```
Open your coding agent in the folder and say:
> Read SETUP.md and set me up.

It checks what you have installed, connects the tools, interviews you to build your profile, and does a test run. Or skip the clone: paste this repo's link into your agent and say the same.

### What you'll set up (the agent guides you)
| Thing | Needed? | Cost |
|---|---|---|
| A coding agent + a model | Yes | **Bring your own.** Use your existing plan or credits, or free models (Gemini CLI login, OpenRouter `:free` models, OpenCode free models). We don't provide credits |
| Exa + Parallel Search MCPs | Yes | Free, no key |
| Your profile (`profile/me.md`) and verified facts (`profile/facts.md`) | Yes | Built for you in an interview, from your resume, GitHub and portfolio |
| Firecrawl MCP | Optional | Free plan, your own key |
| Gmail drafts (Google Workspace MCP) | Optional | Free, your own Google Cloud OAuth client. Drafts only, it can't send |
| Daily scheduling | Optional | `schedule/run.sh` (cron) or `schedule/run.ps1` (Windows Task Scheduler) |

## The rules it follows
- **Never sends anything.** Emails become drafts. You send every email and DM by hand.
- **No invented facts.** Claims about you come only from `profile/facts.md`. Claims about companies have a source URL. Unverified things are labelled.
- **Public reads only** on X and LinkedIn. No logins, cookies or browser automation there, and no automated likes, follows or DMs.
- **Your data stays local.** Your profile, leads, briefs and resumes are gitignored, so forking this repo publicly never leaks your job hunt.
- Free tools first, one call at a time, and it backs off on rate limits.

## Repo map
```
AGENTS.md          the operating manual every agent reads
SETUP.md           first-run setup, written for an agent to follow
prompts/           the workflows (any agent: "read prompts/<name>.md and do it")
playbook/          discovery strategy and outreach rules
profile/           templates for your profile and verified facts
config/            MCP config for Claude Code, OpenCode, Codex, Gemini CLI, Pi
schedule/          headless daily runs
tools/             tiny free helpers (keyless search, read a public X post)
examples/          what a sweep output looks like (fictional)
```
Slash commands: `/funding-sweep`, `/x-sweep`, `/research-company`, `/follow-ups` in Claude Code, OpenCode, Gemini CLI and Pi.

## Honest limits
- A sweep is a long, multi-tool run. Small free models can skip rules or stumble on tools. If results look sloppy, use a stronger model for the sweeps.
- Free search endpoints have rate limits, and some days nothing fits you. That's normal.
- The agent finds and drafts. Getting hired is still on you: proof of work, good follow-ups, and showing up well on calls.

## License
MIT
