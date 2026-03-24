#!/bin/bash
# auto-done.sh — runs /done logic automatically before context compaction
# Called by the PreCompact hook. Reads the current session transcript,
# extracts the conversation, and runs claude -p to write handoff notes.

INPUT=$(cat)
SESSION_ID=$(echo "$INPUT" | jq -r '.session_id // empty')

if [ -z "$SESSION_ID" ]; then
  exit 0
fi

TRANSCRIPT="$HOME/.claude/projects/-Users-jacknosila/${SESSION_ID}.jsonl"

if [ ! -f "$TRANSCRIPT" ]; then
  exit 0
fi

# Extract readable conversation from transcript (last 300 lines)
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

# Write prompt to a temp file to avoid shell argument length issues
PROMPT_FILE=$(mktemp /tmp/auto-done-prompt.XXXXXX)
trap 'rm -f "$PROMPT_FILE"' EXIT

cat "$HOME/.claude/skills/done/SKILL.md" > "$PROMPT_FILE"
printf '\n\nArguments: quick\n\nHere is the full conversation transcript to analyze:\n\n---\n' >> "$PROMPT_FILE"
echo "$CONVERSATION" >> "$PROMPT_FILE"
printf '\n---\n' >> "$PROMPT_FILE"

# Pipe prompt to claude -p via stdin (avoids shell escaping issues)
/Users/jacknosila/.local/bin/claude --dangerously-skip-permissions -p < "$PROMPT_FILE" 2>/dev/null || true
