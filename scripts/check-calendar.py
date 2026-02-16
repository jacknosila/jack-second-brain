#!/usr/bin/env python3
"""
Check Google Calendar for upcoming events
Requires: OAuth2 setup (same as Gmail)
"""

from datetime import datetime, timedelta
import json

def check_calendar_manual():
    """
    Manual calendar check using Google Calendar API
    Will need OAuth2 credentials once we set that up
    """
    print("📅 Calendar Check")
    print("=" * 50)
    print("\n⚠️  Waiting for OAuth2 setup to access Google Calendar")
    print("\nOnce configured, I'll check for:")
    print("  • Events in next 2 hours (urgent alerts)")
    print("  • Events today (morning briefing)")
    print("  • Events tomorrow (evening preview)")
    print("  • Conflicts and overlaps")
    
def format_event(event):
    """Format calendar event for display"""
    start = event.get('start', {})
    summary = event.get('summary', 'No title')
    location = event.get('location', '')
    
    # Handle different time formats
    if 'dateTime' in start:
        start_time = start['dateTime']
        # Parse ISO format
        dt = datetime.fromisoformat(start_time.replace('Z', '+00:00'))
        time_str = dt.strftime('%I:%M %p')
    else:
        time_str = "All day"
    
    output = f"⏰ {time_str} - {summary}"
    if location:
        output += f"\n   📍 {location}"
    
    return output

if __name__ == "__main__":
    check_calendar_manual()
