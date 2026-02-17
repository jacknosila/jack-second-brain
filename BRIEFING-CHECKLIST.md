# Daily Briefing Review Checklist

Use this checklist to verify each daily briefing draft before sending.

## Required Sections (in order)

### 1. Header
- [ ] Date is correct (format: "Day, Month DD, YYYY")
- [ ] Day of week is correct

### 2. Weather Section (🌤️)
- [ ] Current temperature shown (both °C and °F)
- [ ] Weather condition/description present
- [ ] High/Low forecast present
- [ ] No error messages or broken data

### 3. Aave V3 Status (💎)
- [ ] Health Factor shown (or placeholder if not implemented)
- [ ] Total Collateral mentioned
- [ ] Total Debt mentioned
- [ ] Section present (even if placeholder)

### 4. X/Twitter Highlights (🐦)
- [ ] Monitored accounts listed
- [ ] Top posts shown (or placeholder note if not implemented)
- [ ] Section present

### 5. Book Insight (📚)
- [ ] Title/theme present
- [ ] Book sources cited
- [ ] Connection to John's work/interests
- [ ] Tyler Cowen-style insight quality

### 6. Footer
- [ ] "Have a productive day, John!"
- [ ] Signed "— Jack ⚡"

## Common Issues to Check

- [ ] No Python errors or stack traces
- [ ] No [Error: ...] messages in output
- [ ] No missing API data without explanation
- [ ] All sections have proper emoji headers
- [ ] Formatting is clean and readable

## After Approval

```bash
cd /Users/jacknosila/.openclaw/workspace
scripts/send-briefing.sh
```

---

**If any section is broken or missing**: Do NOT send. Fix the issue first or notify John about the problem.
