# Verified facts (grounding file)

Copy to `profile/facts.md`. This is your agent's "context engine": the only place it may take numbers and claims about your work from. If a fact isn't here, the agent must not say it.

Rules for this file:
- One fact per line, with where it comes from (repo, README, notebook, merged PR, offer letter).
- Numbers exactly as measured, with the conditions (hardware, dataset, date).
- If something was rough or partial, say so here, so the agent labels it in outreach.
- Remove anything you no longer want used (old resume metrics you can't back up).

## Projects
| Fact | Source | Date |
|---|---|---|
| | | |

## Open source
| Repo | PR / issue | Status (merged / open) | What it fixed, in plain words |
|---|---|---|---|

## Work
| Fact | Can be said publicly? |
|---|---|

## Things that are NOT true (stop the agent repeating them)
- (e.g. "I never led a team of 10", "that benchmark was on a toy dataset")
