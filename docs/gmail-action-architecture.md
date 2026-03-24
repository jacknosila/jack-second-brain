# Gmail Action Architecture — Options

**Context:** jacknosila@gmail.com receives emails. When an email arrives (especially from John), the system should act on it autonomously.

**Status:** Gmail watcher LaunchAgent is running (checks every 5 min). Currently sends Telegram notification to John's chat — not ideal.

---

## Options

### Option A — Direct claude -p spawn
When new email detected → spawn `claude -p` with email content + instructions.

**Pros:** Full reasoning, can handle anything
**Cons:** Loads full context (CLAUDE.md + memory) for every email — token cost per email even for trivial requests

### Option B — Two-tier (script + claude fallback)
Pattern-match common requests in Python (Aave check, add calendar event, weather, etc.). Only spawn Claude for complex/ambiguous emails.

**Pros:** 90% of routine tasks = zero tokens. Claude only when needed.
**Cons:** Need to maintain the pattern list; edge cases fall through

### Option C — Haiku triage
Use claude-haiku-4-5 (cheap/fast) to parse intent, then either execute a script action or escalate to Sonnet.

**Pros:** Flexible reasoning at low cost for triage
**Cons:** Two-model overhead; more complex

### Option D — Queue + batch processing
Write emails to a queue file. Process in bulk next time the main Claude session is active (triggered by a Telegram message or periodic wakeup).

**Pros:** No extra token cost — piggybacks on existing sessions
**Cons:** Not real-time; latency depends on when next session fires

---

## Current State
- LaunchAgent: `~/Library/LaunchAgents/jack.gmail-watcher.plist` (runs every 5 min)
- Script: `~/jack-second-brain/scripts/gmail-watcher.py`
- Needs: decision on action architecture before wiring up response logic
