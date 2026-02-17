#!/usr/bin/env python3
"""
System Health Check Script
Verifies all Jack Nosila systems are operational
"""

import subprocess
import json
import os
import sys
from pathlib import Path
from datetime import datetime

def run_cmd(cmd, shell=True):
    """Run command and return output"""
    try:
        result = subprocess.run(cmd, shell=shell, capture_output=True, text=True, timeout=10)
        return result.returncode == 0, result.stdout.strip()
    except Exception as e:
        return False, str(e)

def check_cron_jobs():
    """Check cron job status"""
    print("\n🕒 CRON JOBS")
    print("─" * 50)
    
    success, output = run_cmd("openclaw cron list")
    if not success:
        print("❌ Cannot list cron jobs")
        return False
    
    # Parse text table output
    lines = output.strip().split('\n')
    if len(lines) < 2:
        print("❌ No cron jobs found")
        return False
    
    # Skip header line
    job_lines = [l for l in lines[1:] if l.strip()]
    
    if not job_lines:
        print("❌ No cron jobs found")
        return False
    
    print(f"✅ Found {len(job_lines)} cron job(s)")
    for line in job_lines:
        parts = line.split()
        if len(parts) >= 2:
            name = ' '.join(parts[1:4])  # Approximate name extraction
            status = parts[-4] if len(parts) > 6 else "unknown"
            print(f"   • {name[:40]} (status: {status})")
    
    return True

def check_email():
    """Check email monitoring"""
    print("\n📧 EMAIL MONITORING")
    print("─" * 50)
    
    # Check credentials file
    creds_path = Path.home() / ".openclaw/workspace/.credentials/jack.env"
    if not creds_path.exists():
        print("❌ Credentials file missing")
        return False
    print("✅ Credentials file exists")
    
    # Check heartbeat state
    state_path = Path.home() / ".openclaw/workspace/memory/heartbeat-state.json"
    if state_path.exists():
        try:
            with open(state_path) as f:
                state = json.load(f)
            last_gmail = state.get("lastChecks", {}).get("email_gmail")
            if last_gmail:
                last_time = datetime.fromtimestamp(last_gmail)
                print(f"✅ Last Gmail check: {last_time.strftime('%Y-%m-%d %H:%M:%S')}")
            else:
                print("⚠️  No Gmail check timestamp")
        except Exception as e:
            print(f"⚠️  Cannot read heartbeat state: {e}")
    else:
        print("⚠️  Heartbeat state file missing")
    
    return True

def check_git():
    """Check git repository status"""
    print("\n🔧 GIT REPOSITORY")
    print("─" * 50)
    
    workspace = Path.home() / ".openclaw/workspace"
    os.chdir(workspace)
    
    # Check remote
    success, output = run_cmd("git remote -v")
    if not success or not output:
        print("❌ No git remote configured")
        return False
    print("✅ Remote configured")
    
    # Check status
    success, output = run_cmd("git status -sb")
    if success:
        print(f"   {output}")
    
    # Check last commit
    success, output = run_cmd("git log -1 --format='%ar: %s'")
    if success:
        print(f"✅ Last commit: {output}")
    
    return True

def check_scripts():
    """Check required scripts exist"""
    print("\n📝 SCRIPTS")
    print("─" * 50)
    
    workspace = Path.home() / ".openclaw/workspace"
    scripts = [
        "scripts/generate-daily-briefing-v2.py",
        "scripts/send-email.py",
        "scripts/x-top-posts.py"
    ]
    
    all_exist = True
    for script in scripts:
        path = workspace / script
        if path.exists():
            print(f"✅ {script}")
        else:
            print(f"❌ {script} missing")
            all_exist = False
    
    return all_exist

def check_memory():
    """Check memory files"""
    print("\n🧠 MEMORY FILES")
    print("─" * 50)
    
    workspace = Path.home() / ".openclaw/workspace"
    
    # Check MEMORY.md
    memory_md = workspace / "MEMORY.md"
    if memory_md.exists():
        print(f"✅ MEMORY.md exists")
    else:
        print(f"❌ MEMORY.md missing")
    
    # Check today's daily note
    today = datetime.now().strftime("%Y-%m-%d")
    daily_note = workspace / "memory" / f"{today}.md"
    if daily_note.exists():
        print(f"✅ Today's note: memory/{today}.md")
    else:
        print(f"⚠️  No note yet for memory/{today}.md")
    
    return True

def main():
    """Run all health checks"""
    print("=" * 50)
    print("   JACK NOSILA SYSTEM HEALTH CHECK")
    print("   " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 50)
    
    checks = [
        ("Cron Jobs", check_cron_jobs),
        ("Email", check_email),
        ("Git", check_git),
        ("Scripts", check_scripts),
        ("Memory", check_memory),
    ]
    
    results = []
    for name, check_func in checks:
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print(f"\n❌ {name} check failed: {e}")
            results.append((name, False))
    
    # Summary
    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {name}")
    
    all_passed = all(r[1] for r in results)
    
    if all_passed:
        print("\n🎉 All systems operational!")
        return 0
    else:
        print("\n⚠️  Some checks failed - review above")
        return 1

if __name__ == "__main__":
    sys.exit(main())
