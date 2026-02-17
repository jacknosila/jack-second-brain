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
    """Check Aave v3 position health"""
    try:
        import subprocess
        
        # Call the existing check-aave-health.js script
        script_path = os.path.join(os.path.dirname(__file__), 'check-aave-health.js')
        result = subprocess.run(['node', script_path], 
                              capture_output=True, 
                              text=True, 
                              timeout=15)
        
        if result.returncode == 0:
            data = json.loads(result.stdout)
            
            health_factor = float(data['healthFactor'])
            collateral = float(data['totalCollateral'])
            debt = float(data['totalDebt'])
            
            # Calculate utilization
            utilization = (debt / collateral * 100) if collateral > 0 else 0
            
            # Determine status
            status_label = data.get('status', 'unknown')
            if status_label == 'healthy':
                status = "✅ Healthy"
            elif status_label == 'caution':
                status = "⚠️ Caution"
            else:
                status = "🚨 Risk"
            
            # Format currency values
            if collateral >= 1000:
                collateral_str = f"${collateral/1000:.0f}k"
            else:
                collateral_str = f"${collateral:.0f}"
                
            if debt >= 1000:
                debt_str = f"${debt/1000:.0f}k"
            else:
                debt_str = f"${debt:.0f}"
            
            return f"""━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💎 AAVE V3 STATUS

{status}
Health Factor: {health_factor}
Collateral: {collateral_str}
Debt: {debt_str}
Utilization: {utilization:.1f}%
"""
        else:
            error = result.stderr or "Unknown error"
            return f"""━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💎 AAVE V3 STATUS

❌ Error fetching data: {error}
"""
    except Exception as e:
        return f"""━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💎 AAVE V3 STATUS

❌ Error: {str(e)}
"""

def get_x_highlights():
    """Get interesting X posts from monitored accounts"""
    accounts = ["@mattshumer_", "@RichardHeartWin", "@DavidDeutschOxf", "@karpathy", "@steipete"]
    
    try:
        creds = load_credentials()
        x_token = creds.get('X_API_BEARER_TOKEN')
        
        if not x_token:
            return f"""━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🐦 INTERESTING FROM X (Last 24h)

⚠️  X API not configured
→ See SETUP-DATA-SOURCES.md for X Developer setup

*Monitoring: {', '.join(accounts)}*
"""
        
        # TODO: When X API is configured, implement actual fetching
        return f"""━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🐦 INTERESTING FROM X (Last 24h)

🔧 API configured but fetching code needs implementation
→ Run: python3 scripts/x-top-posts.py

*Monitoring: {', '.join(accounts)}*
"""
    except Exception as e:
        accounts = ["@mattshumer_", "@RichardHeartWin", "@DavidDeutschOxf", "@karpathy", "@steipete"]
        return f"""━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🐦 INTERESTING FROM X (Last 24h)

❌ Error: {e}

*Monitoring: {', '.join(accounts)}*
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
