# MEMORY.md - Long-Term Memory

_Curated memories and insights that persist across sessions._

## About John
- Physicist at CMU, works on CMS experiment at the Large Hadron Collider
- Values efficiency and directness (no fuss about formalities)
- Invested significant effort in setting up this system
- Wants help with: assistant tasks, building a second brain, learning new things

## Preferences
- **Calendar**: Don't proactively alert about events - only when asked
- **Email**: Process emails immediately during heartbeat checks - don't just alert, take action

## About Me (Jack)
- Name: Jack Nosila
- Vibe: Tyler Cowen-style — curious, efficient, connecting ideas
- Role: teacher, helper, builder
- Signature: ⚡

## Key Milestones
- **2026-02-16**: Gmail account approved! (jacknosila@gmail.com) - mainstream email platform access

## Email Infrastructure
- **Primary (sending)**: jacknosila@gmail.com (SMTP, approved Feb 16, 2026)
- **Fallback (sending)**: jacknosila@agentmail.to (API)
- **Monitoring (receiving)**: jacknosila@agentmail.to (checked every 60-90 min)
- **Legacy**: jacknosila@proton.me (original, unused)

## Daily Briefing Configuration
- **X Accounts Monitored**: @mattshumer_ @RichardHeartWin @DavidDeutschOxf @karpathy @steipete
- **Format**: Top 1-2 most interesting posts from last 24h (replaces software news section)
- **Workflow (Updated 2026-02-17)**:
  - 7:30 AM EST: Cron generates draft and sends to me for review
  - I proofread: check weather, X highlights, email status, book insight
  - After approval: run `scripts/send-briefing.sh` to send to johnda102@gmail.com
  - Archive sent briefings to `memory/briefings/YYYY-MM-DD.txt`
- **Reason**: Ensure quality control - no broken weather data or missing sections

## API Cost Optimization (2026-02-16)
- **Main session:** Claude Sonnet 4.5 (high quality for conversations)
- **Automated tasks:** Claude Haiku 4 (12x cheaper for cron jobs, heartbeats)
- **Heartbeat frequency:** Reduced from every 30 min to every 90-120 min
- **Expected savings:** 60-80% reduction in API costs
- **Documentation:** docs/cost-optimization.md

## Key Learnings
- **Heartbeat monitoring**: Check email ~every 90-120 mins during day (cost-optimized from 60-90), rotate through different services
- **Ad-hoc commits**: Commit meaningful updates organically, not just at midnight
- **AgentMail API**: Labels filter works (`?labels=unread`), use v0 endpoint path
- **Calendar events**: Always create on johnda102@gmail.com (John's calendar), not jacknosila@gmail.com
- **OpenAI acquisition**: Peter Steinberger (OpenClaw creator) joined OpenAI Feb 15, 2026 - project stays open source (foundation model)
