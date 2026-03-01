# Automation Schedule (OpenClaw)

_Last updated: 2026-02-28_

## Daily / Periodic Jobs

### 1) Daily briefing (validated)
- **Name:** daily-briefing-validated-630am
- **Schedule:** 6:30 AM America/New_York (cron: `30 6 * * *`)
- **Action:** Generate + validate + email the daily briefing
- **Notes:** Sends only if validation passes; alerts on failure

### 2) Daily journal entry (manual habit)
- **Name:** daily-journal
- **Schedule:** End of day (manual, but expected daily)
- **Action:** Write a short journal entry in `second-brain/memory/YYYY-MM-DD.md` with what I did + interesting thoughts
- **Notes:** Commit + push after writing

### 3) Second brain backup
- **Name:** second-brain-backup
- **Schedule:** Every 6 hours
- **Action:** Commit + push second-brain repo

### 4) Second brain update pull
- **Name:** update-second-brain
- **Schedule:** Every 24 hours
- **Action:** `git pull` latest changes to second-brain repo

### 4) Gmail monitor (John whitelist)
- **Name:** gmail-monitor-john
- **Schedule:** Every 30 minutes
- **Action:** Check unread mail from johnda102@gmail.com and execute instructions
- **Notes:** Silent unless action taken or clarification needed

### 5) Proton Mail monitor
- **Name:** proton-mail-action
- **Schedule:** Every 60 minutes
- **Action:** Check Proton Mail inbox for actionable messages
- **Notes:** Silent unless action taken or clarification needed

### 6) RoamNotes sync & summary
- **Name:** roam-notes-sync
- **Schedule:** 11:30 PM America/New_York (cron: `30 23 * * *`)
- **Action:** Pull RoamNotes + summarize recent changes
- **Notes:** Delivery announce mode (may require tweaks if delivery fails)

---

## Where this lives
- OpenClaw cron config: `~/.openclaw/cron/jobs.json`

If you want changes, tell me which job and new schedule.
