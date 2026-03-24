---
name: start
description: |
  Orient a new session from handoff notes and current priorities.
  Read this at the start of every session to resume context without
  re-explaining anything.
version: 1.0.0
---

# /start — Session Orientation

Get up to speed quickly and identify the single most important next step.

## Step 1: Read Handoff

Read `~/jack-second-brain/handoff.md` in full. This is the source of truth for
what the last session accomplished and where to resume.

## Step 2: Scan for Open Follow-ups

Read `~/jack-second-brain/session-log.md` and find all unchecked action items
(`- [ ]`) from the 3 most recent entries. Ignore completed items (`- [x]`).

## Step 3: Deliver the Briefing

Output a compact, scannable briefing — no waffle, no padding:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 Session Start — <Day, DD Month YYYY>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Last session: <1 sentence from handoff>

▶ Resume here
  <The single most important next step, verbatim from handoff if clear>

Open follow-ups
  • <item 1>
  • <item 2>  (or "None" if clean)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Step 5: Ask One Question

After the briefing, ask exactly one question:

> Shall we pick up where we left off, or is there something else on your mind?

Then wait. Do not take any further action until the user responds.
