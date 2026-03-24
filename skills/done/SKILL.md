---
name: done
description: |
  Session capture with handoff notes and archive pruning.
  Extracts decisions, open questions, follow-ups, and modified files
  from the current session, appends them to the session log, and
  writes a condensed handoff summary for the next session.
version: 1.2.0
argument-hint: "[quick] [project:name]"
---

# /done — Session Capture

Capture the current session and prepare handoff notes for continuity.

## Arguments

- No arguments — full capture including context summaries
- `quick` — abbreviated output, skip context summaries
- `project:name` — tag the entry with a specific project label

## Files

| File | Purpose |
|------|---------|
| `~/jack-second-brain/session-log.md` | Running log of all sessions, newest-first |
| `~/jack-second-brain/handoff.md` | Overwritten each session; read at start of next session |
| `~/jack-second-brain/session-log-archive.md` | Entries pruned from the log after 60 days |

---

## Step 1: Scope Identification

Review the full conversation to identify:
- **Topic / theme** of this session (1 sentence)
- **Projects touched** (e.g., `~/RoamNotes`, `~/NotesWebpage`, `CLAUDE.md`, etc.)
- **Session length** estimate (short / medium / long)
- **Project tag** — use `$ARGUMENTS` if `project:name` was passed, otherwise infer from files touched

---

## Step 2: Artifact Extraction

Scan the conversation for:

- **Decisions made** — confirmed choices, configurations, commitments (not tentative ideas)
- **Open questions** — unresolved items that need future attention
- **Follow-ups** — concrete next steps or action items
- **Files created or modified** — list paths relative to `~`

If `quick` is in `$ARGUMENTS`, skip context summaries and list only bullet points.

---

## Step 3: Append Entry to Session Log

Read the existing log (create if missing), then prepend a new entry at the top:

```bash
touch ~/jack-second-brain/session-log.md
```

Format the entry as:

```markdown
## YYYY-MM-DD — <Topic> [project:<tag>]

**Decisions**
- <decision 1>
- <decision 2>

**Open Questions**
- <question 1>

**Follow-ups**
- [ ] <action item 1>
- [ ] <action item 2>

**Files Modified**
- `~/path/to/file`

---
```

Prepend this block to the top of `~/jack-second-brain/session-log.md`, preserving all existing content below it.

---

## Step 4: Write Handoff File

Overwrite `~/jack-second-brain/handoff.md` with a condensed summary for the *next* session to read:

```markdown
# Handoff — YYYY-MM-DD

## Last Session
<1–2 sentence summary of what was accomplished>

## Resume Here
<The single most important next step, stated concisely>

## Open Items
- <item 1>
- <item 2>

## Context
- Projects touched: <list>
- Key files: <list>
```

---

## Step 5: Archive Pruning

Check for entries in `~/jack-second-brain/session-log.md` older than 60 days:

```bash
# Entries are dated by the ## YYYY-MM-DD header line
```

Move any entries with dates older than 60 days from today to the bottom of `~/jack-second-brain/session-log-archive.md`. Remove them from the main log. Report how many entries were archived.

---

## Step 6: Git Commit and Push

Commit and push all changes in `~/jack-second-brain/` with a message summarising the session:

```bash
cd ~/jack-second-brain && git add -A && git commit -m "done: <topic> (<date>)" && git push origin master
```

Use the session topic from Step 1 as `<topic>`. If the commit or push fails, report the error
but do not abort — the files are already written.

---

## Step 7: Report

Print a brief confirmation:

```
✓ Session captured  (<date>)
  Topic:     <topic>
  Project:   <tag>
  Decisions: <N>
  Follow-ups: <N>
  Archived:  <N> old entries

Handoff written → ~/jack-second-brain/handoff.md
```
