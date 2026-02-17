#!/usr/bin/env python3
"""
Generate daily briefing with book-based insights (Tyler Cowen style)
"""

import warnings
warnings.filterwarnings('ignore', category=UserWarning)

import sys
import os
import json
import requests
from datetime import datetime, timedelta

# Add book insights module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from book_insights import get_daily_insight

# Load credentials from environment
def load_credentials():
    """Load credentials from jack.env file"""
    creds = {}
    creds_file = os.path.expanduser('~/.openclaw/workspace/.credentials/jack.env')
    
    with open(creds_file) as f:
        for line in f:
            line = line.strip()
            if '=' in line and not line.startswith('#'):
                key, value = line.split('=', 1)
                creds[key] = value.strip('"')
    
    return creds

def get_weather():
    """Fetch Pittsburgh weather"""
    try:
        # Using wttr.in for simple weather API
        url = "https://wttr.in/Pittsburgh?format=j1"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            current = data['current_condition'][0]
            
            temp_c = current['temp_C']
            temp_f = current['temp_F']
            desc = current['weatherDesc'][0]['value']
            
            # Today's forecast
            today = data['weather'][0]
            high_c = today['maxtempC']
            high_f = today['maxtempF']
            low_c = today['mintempC']
            low_f = today['mintempF']
            
            return f"""━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌤️  WEATHER TODAY (Pittsburgh)

Current: {temp_c}°C ({temp_f}°F), {desc.lower()}
High: {high_c}°C ({high_f}°F) | Low: {low_c}°C ({low_f}°F)
"""
    except Exception as e:
        return f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n🌤️  WEATHER\n\n[Error fetching weather: {e}]\n"

def get_aave_status():
    """Check Aave v3 position health (placeholder)"""
    # This would query Aave API or on-chain data
    # For now, return placeholder
    return """━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💎 AAVE V3 STATUS

Health Factor: [To be implemented]
Total Collateral: [Query on-chain]
Total Debt: [Query on-chain]

*Note: Add Aave position monitoring script*
"""

def get_x_highlights():
    """Get interesting X posts from monitored accounts"""
    accounts = ["@mattshumer_", "@RichardHeartWin", "@DavidDeutschOxf", "@karpathy", "@steipete"]
    
    return f"""━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🐦 INTERESTING FROM X (Last 24h)

*Monitoring: {', '.join(accounts)}*

[Top 1-2 posts will appear here once X scraping is implemented]

*Note: Requires web scraping or X API access*
"""

def check_emails():
    """Check AgentMail for unread messages"""
    try:
        creds = load_credentials()
        api_key = creds.get('AGENTMAIL_API_KEY')
        inbox_id = creds.get('AGENTMAIL_INBOX_ID')
        
        url = f"https://api.agentmail.to/v0/inboxes/{inbox_id}/messages?labels=unread&limit=5"
        headers = {"Authorization": f"Bearer {api_key}"}
        
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            count = data.get('count', 0)
            
            if count == 0:
                return "✅ Inbox zero\n"
            
            messages = data.get('messages', [])
            email_list = ""
            for msg in messages[:3]:  # Top 3
                from_addr = msg.get('from', 'Unknown')
                subject = msg.get('subject', 'No subject')
                email_list += f"  • From {from_addr}: {subject}\n"
            
            if count > 3:
                email_list += f"  • ... and {count - 3} more\n"
            
            return f"📧 {count} unread message(s):\n{email_list}"
    except Exception as e:
        return f"❌ Error checking email: {e}\n"

def generate_briefing():
    """Generate complete daily briefing"""
    
    now = datetime.now()
    date_str = now.strftime("%B %d, %Y")
    day_str = now.strftime("%A")
    
    # Build briefing sections
    weather_section = get_weather()
    aave_section = get_aave_status()
    x_highlights = get_x_highlights()
    book_insight = get_daily_insight()
    
    briefing = f"""DAILY BRIEFING - {day_str}, {date_str}

{weather_section}
{aave_section}
{x_highlights}

{book_insight}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Have a productive day, John!

— Jack ⚡
"""
    
    return briefing

if __name__ == "__main__":
    print(generate_briefing())
