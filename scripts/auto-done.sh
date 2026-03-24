#!/bin/bash
# auto-done.sh — runs /done logic automatically before context compaction
# Called by the PreCompact hook. Reads the current session transcript,
# extracts the conversation, and runs claude -p to write handoff notes.

set -e

# Read session_id from hook stdin
INPUT=$(cat)
SESSION_ID=$(echo "$INPUT" | jq -r '.session_id // empty')

if [ -z "$SESSION_ID" ]; then
  exit 0
fi

PROJECT_DIR="$HOME/.claude/projects/-Users-jacknosila"
TRANSCRIPT="$PROJECT_DIR/${SESSION_ID}.jsonl"

if [ ! -f "$TRANSCRIPT" ]; then
  exit 0
fi

# Extract readable conversation from transcript (last 300 exchanges max)
CONVERSATION=$(jq -r '
  select(.type == "user" or .type == "assistant") |
  if .type == "user" then
    "USER: " + (
      if (.message.content | type) == "string" then .message.content
      elif (.message.content | type) == "array" then
        [.message.content[] | select(.type == "text") | .text] | join(" ")
      else "" end
    )
  else
    "ASSISTANT: " + (
      if (.message.content | type) == "string" then .message.content
      elif (.message.content | type) == "array" then
        [.message.content[] | select(.type == "text") | .text] | join(" ")
      else "" end
    )
  end
' "$TRANSCRIPT" 2>/dev/null | tail -300)

if [ -z "$CONVERSATION" ]; then
  exit 0
fi

# Get the /done skill instructions
DONE_SKILL=$(cat "$HOME/.claude/skills/done/SKILL.md")

# Run claude -p with the done skill + conversation transcript
# Use quick mode to avoid overly long output
/Users/jacknosila/.local/bin/claude -p "$(printf '%s\n\nArguments: quick\n\nHere is the full conversation transcript to analyze:\n\n---\n%s\n---' "$DONE_SKILL" "$CONVERSATION")" 2>/dev/null || true
