# Handoff — 2026-03-23

## Last Session
Set up PreCompact and PostCompact hooks in `~/.claude/settings.json`. PreCompact spawns a claude subprocess with the /done skill prompt piped via stdin, reading the session transcript JSONL to write handoff notes automatically. PostCompact injects handoff.md + open follow-ups back into context.

## Resume Here
Verify the PreCompact hook fires correctly during a real autocompact event — check that `handoff.md` and `session-log.md` are written properly.

## Open Items
- Confirm PreCompact hook triggers reliably in production compaction
- Confirm PostCompact injects handoff content correctly after compaction

## Context
- Projects touched: claude-code-hooks, jack-second-brain
- Key files: `~/jack-second-brain/scripts/auto-done.sh`, `~/.claude/settings.json`
