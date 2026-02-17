# API Cost Optimization

**Implemented:** 2026-02-16

## Changes Made

### 1. Model Configuration
- **Main session (interactive):** Claude Sonnet 4.5 ($3/M in, $15/M out)
- **Automated tasks (cron, subagents):** Claude Haiku 4 ($0.25/M in, $1.25/M out)

**Savings:** ~12x cheaper for routine tasks

### 2. Heartbeat Frequency
- **Before:** Every 30 minutes (16 checks/day)
- **After:** Every 90-120 minutes (8-10 checks/day)

**Savings:** ~40% reduction in heartbeat API calls

### 3. What Uses What

**Claude Sonnet 4.5 (expensive, high quality):**
- Direct conversations with John
- Complex analysis and synthesis
- Book insights generation
- Paper summaries
- Strategic decision-making

**Claude Haiku 4 (cheap, fast):**
- Daily briefing generation (7 AM cron)
- Daily git commit (10 PM cron)
- Email heartbeat checks
- Script execution tasks
- Simple automation

## Expected Cost Reduction

**Before optimization:**
- Interactive: ~$X/day
- Heartbeats: 16 × Sonnet = ~$Y/day
- Cron jobs: 2 × Sonnet/day = ~$Z/day
- **Total: ~$X+Y+Z/day**

**After optimization:**
- Interactive: ~$X/day (unchanged)
- Heartbeats: 10 × Haiku = ~$Y/12/day
- Cron jobs: 2 × Haiku/day = ~$Z/12/day
- **Total: ~$X + (Y+Z)/12/day**

**Estimated savings: 60-80% overall** (depending on interactive usage)

## Configuration

### openclaw.json
```json
{
  "agents": {
    "defaults": {
      "model": {
        "primary": "anthropic/claude-sonnet-4-5-20250929"
      },
      "models": {
        "anthropic/claude-sonnet-4-5-20250929": {},
        "anthropic/claude-haiku-4-20250514": {}
      },
      "subagents": {
        "model": {
          "primary": "anthropic/claude-haiku-4-20250514"
        }
      }
    }
  }
}
```

### HEARTBEAT.md
- Check every 3-4 heartbeats (90-120 min intervals)
- Reduced from 2-3 heartbeats (60-90 min)

## Monitoring

Track actual costs via Anthropic dashboard:
- https://console.anthropic.com/settings/billing

Compare before/after over 7-day periods.

## Future Optimizations

If costs still high:
1. **Switch main session to Sonnet 3.5** ($3/M in, $15/M out → same, but could use older cheaper version)
2. **More aggressive context compaction** (reduce token usage per conversation)
3. **Disable heartbeat checks entirely** (manual email checking only)
4. **Move briefing to pure Python** (no LLM call, just script execution)

## Reverting

If quality suffers on automated tasks:
```bash
# Edit openclaw.json, remove subagents.model section
# Restart: openclaw gateway restart
```

This will revert to Sonnet for everything.
