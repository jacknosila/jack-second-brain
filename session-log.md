## 2026-03-24 — Gmail watcher, Hue lights, Oura ring setup [project:home-automation]

**Decisions**
- Skills (done/start) moved to `~/jack-second-brain/skills/` with symlinks back to `~/.claude/skills/`
- `gmail-watcher.py` built: polls inbox every 5 min, sends Telegram notification on new emails
- Hue bridge API key obtained (bridge at 192.168.1.159); lights controllable via REST API
- Gmail autonomous action architecture deferred — John wants to think through options (spawn `claude -p` per email vs other approaches)

**Open Questions**
- Gmail watcher: spawn `claude -p` per email has context loading cost — is it worth it vs lighter alternatives?
- Oura ring personal access token still needs to be created via developer portal

**Follow-ups**
- [ ] Decide on Gmail watcher architecture and implement chosen approach
- [ ] Create Oura personal access token and test API read

**Files Modified**
- `~/jack-second-brain/skills/done/SKILL.md`
- `~/jack-second-brain/skills/start/SKILL.md`
- `~/jack-second-brain/scripts/auto-done.sh`
- `~/jack-second-brain/gmail-watcher.py`

---

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
