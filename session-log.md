## 2026-03-23 — Auto-done PreCompact hook setup [project:claude-code-hooks]

**Decisions**
- PreCompact hook runs `auto-done.sh` which spawns `claude -p` with the /done prompt piped via stdin, passing the session transcript as context
- PostCompact hook injects `handoff.md` + open follow-ups from `session-log.md` into model context automatically
- Script uses `--dangerously-skip-permissions` flag so claude can write files without prompts
- Prompt passed via stdin to avoid shell escaping issues with large strings

**Open Questions**
- Whether the PreCompact hook triggers reliably in all compaction scenarios (not yet confirmed in production)

**Follow-ups**
- [ ] Verify PreCompact hook fires correctly during a real autocompact event
- [ ] Test that handoff.md content is injected correctly on PostCompact

**Files Modified**
- `~/jack-second-brain/scripts/auto-done.sh`
- `~/.claude/settings.json` (PreCompact + PostCompact hooks)

---
