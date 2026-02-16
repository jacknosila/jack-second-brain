# Daily Briefing Configuration

## Schedule
- **Time**: 7:00 AM EST daily (via cron)
- **Delivery**: Email to johnda102@gmail.com via AgentMail

## Sections

### 1. Calendar
- Today's events
- Meetings in next 2 hours (urgent)
- Conflicts or overlaps

### 2. Email Summary
- Unread count from AgentMail
- Unread count from Gmail (when OAuth complete)
- Important messages requiring action

### 3. Interesting X Posts (NEW!)
**Monitored Accounts:**
- `@mattshumer_` - AI/ML developments
- `@RichardHeartWin` - Crypto/Finance
- `@DavidDeutschOxf` - Physics/Philosophy
- `@karpathy` - AI/ML insights
- `@steipete` - Tech/iOS development

**Selection Criteria:**
- Prioritize posts related to:
  - Physics research
  - AI/ML breakthroughs
  - Open source releases
  - Interesting technical discussions
- Show top 1-2 most interesting posts from last 24 hours

**Implementation:**
- Use `web_search` tool during briefing generation
- Search for recent posts from each account
- Rank by relevance to John's interests
- Format as brief quotes with context

### 4. Action Items
- Extracted from emails
- Upcoming deadlines
- Follow-ups needed

## Generation Method

During briefing generation, I will:
1. Check Google Calendar for today's schedule
2. Query AgentMail API for unread messages
3. Use `web_search` to find recent posts from monitored X accounts
4. Rank and select top 1-2 most interesting posts
5. Compile into formatted email
6. Send via AgentMail to johnda102@gmail.com

## Files
- `scripts/generate-daily-briefing.py` - Main generation script
- `scripts/send-daily-briefing.py` - Sending via AgentMail
- `scripts/fetch-x-posts-simple.py` - Account list

## Note on X/Twitter Access

X/Twitter API requires paid access. Instead, I'll use:
- Web search to find recent public posts
- Focus on quality over quantity (top 1-2 posts only)
- Smart ranking based on John's research interests
