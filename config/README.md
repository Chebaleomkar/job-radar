# config/

One MCP config per CLI. SETUP.md says which file goes where.

Exa and Parallel are keyless by default. To use your own key (higher limits), add an auth header:

| CLI | Header syntax (key read from your environment) |
|---|---|
| Claude Code (`.mcp.json`) | `"headers": { "Authorization": "Bearer ${EXA_API_KEY}" }` |
| OpenCode (`opencode.json`) | `"headers": { "Authorization": "Bearer {env:EXA_API_KEY}" }` |
| Codex (`config.toml`) | `bearer_token_env_var = "EXA_API_KEY"` |
| Gemini CLI (`settings.json`) | `"headers": { "Authorization": "Bearer $EXA_API_KEY" }` (env expansion in headers not confirmed in Gemini's docs; if it fails, use Exa's `?exaApiKey=` URL parameter from your shell profile instead) |
| Pi (`mcp.json`) | `"headers": { "Authorization": "Bearer ${EXA_API_KEY}" }` |

Same pattern for Parallel with `PARALLEL_API_KEY`.

Don't use a service you skipped: delete its block (`firecrawl`, `google`) so the agent doesn't error on start.

Gmail runs with `--permissions gmail:drafts`: read mail and write drafts, no send. Don't raise it to `send`.
