#!/usr/bin/env bash
# Run one job-radar workflow headless. Usage: schedule/run.sh <agent> <workflow>
#   agent:    claude | opencode | codex | gemini | pi
#   workflow: funding-sweep | x-sweep | follow-ups
# Example cron line (daily 10:17): 17 10 * * * /path/to/job-radar/schedule/run.sh claude funding-sweep
set -euo pipefail
cd "$(dirname "$0")/.."
[ -f .env ] && set -a && . ./.env && set +a

agent="${1:?agent}"; wf="${2:?workflow}"
prompt="Read AGENTS.md, then read prompts/$wf.md and do exactly what it says. This is an unattended scheduled run: never send anything, only write files and drafts."
mkdir -p logs; log="logs/$(date +%F)-$wf.log"

case "$agent" in
  claude)   claude -p "$prompt" --allowedTools "Read,Write,Edit,Glob,Grep,WebFetch,WebSearch,Bash(python:*),Bash(nslookup:*),mcp__exa,mcp__parallel,mcp__firecrawl,mcp__google" ;;
  opencode) opencode run --auto "$prompt" ;;
  codex)    codex exec --sandbox workspace-write "$prompt" ;;
  gemini)   gemini -p "$prompt" --approval-mode yolo ;;
  pi)       pi -p -a "$prompt" ;;
  *) echo "unknown agent: $agent" >&2; exit 2 ;;
esac >>"$log" 2>&1
