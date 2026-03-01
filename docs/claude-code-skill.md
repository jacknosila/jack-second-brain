# Claude Code Skill (MCP) — Install Notes

**Date:** 2026-03-01

## What was done
- Cloned: `~/workspace/skills/openclaw-claude-code-skill`
- Installed deps + built + linked globally (`npm link`)
- Added missing runtime deps:
  - `@modelcontextprotocol/sdk`
  - `zod`, `zustand`, `idb-keyval`
- Adjusted TS config to build cleanly (ESNext + Bundler, strict off).
- Relaxed Zod schema typings in `src/mcp/types.ts` (removed explicit `ZodType<>` annotations) to fix TS errors.

## CLI
- Command available: `claude-code-skill`

## Backend API
- Expects MCP backend API server (default URL per README):
  - `http://127.0.0.1:18795`
- Override via env:
  - `BACKEND_API_URL` or `CLAUDE_CODE_API_URL`

## Next steps
- Start/confirm MCP backend server
- Test connection:
  - `claude-code-skill status`
  - `claude-code-skill tools`

