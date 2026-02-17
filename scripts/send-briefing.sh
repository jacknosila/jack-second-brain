#!/bin/bash
# Send the approved daily briefing to John

BRIEFING_FILE="/tmp/daily-briefing-draft.txt"
DATE_STR=$(date +'%B %d, %Y')

if [ ! -f "$BRIEFING_FILE" ]; then
    echo "❌ No briefing draft found at $BRIEFING_FILE"
    exit 1
fi

echo "📧 Sending daily briefing to John..."
cd /Users/jacknosila/.openclaw/workspace/scripts
python3 send-email.py johnda102@gmail.com "Daily Briefing - $DATE_STR" "$BRIEFING_FILE"

if [ $? -eq 0 ]; then
    echo "✅ Briefing sent successfully!"
    # Archive the sent briefing
    mkdir -p /Users/jacknosila/.openclaw/workspace/memory/briefings
    cp "$BRIEFING_FILE" "/Users/jacknosila/.openclaw/workspace/memory/briefings/$(date +'%Y-%m-%d').txt"
else
    echo "❌ Failed to send briefing"
    exit 1
fi
