# Run one job-radar workflow headless on Windows.
# Usage: powershell -File schedule\run.ps1 -Agent claude -Workflow funding-sweep
# Schedule it daily at 10:17 (run once in PowerShell, from the job-radar folder):
#   schtasks /Create /SC DAILY /ST 10:17 /TN "job-radar funding" /TR "powershell -NoProfile -File `"$PWD\schedule\run.ps1`" -Agent claude -Workflow funding-sweep"
param(
  [Parameter(Mandatory)][ValidateSet('claude','opencode','codex','gemini','pi')][string]$Agent,
  [Parameter(Mandatory)][ValidateSet('funding-sweep','x-sweep','follow-ups')][string]$Workflow
)
Set-Location (Split-Path $PSScriptRoot -Parent)
if (Test-Path .env) {
  Get-Content .env | Where-Object { $_ -match '^\s*([A-Z_]+)=(.+)$' } | ForEach-Object {
    [Environment]::SetEnvironmentVariable($Matches[1], $Matches[2].Trim())
  }
}
$prompt = "Read AGENTS.md, then read prompts/$Workflow.md and do exactly what it says. This is an unattended scheduled run: never send anything, only write files and drafts."
New-Item -ItemType Directory -Force logs | Out-Null
$log = "logs\$(Get-Date -Format yyyy-MM-dd)-$Workflow.log"

switch ($Agent) {
  'claude'   { claude -p $prompt --allowedTools "Read,Write,Edit,Glob,Grep,WebFetch,WebSearch,Bash(python:*),Bash(nslookup:*),mcp__exa,mcp__parallel,mcp__firecrawl,mcp__google" *>> $log }
  'opencode' { opencode run --auto $prompt *>> $log }
  'codex'    { codex exec --sandbox workspace-write $prompt *>> $log }
  'gemini'   { gemini -p $prompt --approval-mode yolo *>> $log }
  'pi'       { pi -p -a $prompt *>> $log }
}
