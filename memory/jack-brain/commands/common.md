# Common Commands

## Configuration

```bash
# Get current config
jq '.' ~/.openclaw/openclaw.json

# Check specific config path
jq '.agents.defaults.models' ~/.openclaw/openclaw.json

# View config schema
openclaw config schema > /tmp/schema.json
```

## Daily Briefing / Cron

```bash
# List cron jobs
openclaw cron list

# Test a job manually
openclaw cron run <job-id>
```

## Git

```bash
# Stage all changes
git add -A

# Commit with message
git commit -m "message"

# Check status
git status
```

## Node.js

```bash
# Run a script
node path/to/script.js

# Install dependencies
npm install package-name
```

## Brave Search API

- Key location: `tools.web.search.apiKey` in config
- Works with tier upgrades (free tier has rate limits)
- Test with `web_search` tool

## Memory Management

- Daily logs: `memory/YYYY-MM-DD.md`
- Long-term: `MEMORY.md` (main session only)
- Second brain: `memory/jack-brain/`

---

_Last updated: 2026-02-15_
