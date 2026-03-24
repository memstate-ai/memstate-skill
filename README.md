# Memstate AI Skill

> Persistent, versioned memory for AI agents — alternative to the MCP plugin.

[![memstate.ai](https://img.shields.io/badge/memstate.ai-docs-blue)](https://memstate.ai/docs)
[![GitHub](https://img.shields.io/badge/github-memstate--mcp-black)](https://github.com/memstate-ai/memstate-mcp)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

This is an **AgentSkill** (a `SKILL.md`-based skill) for AI coding agents (Cline, Cursor, Kilo, Manus, OpenClaw, etc.) that provides full access to [Memstate AI](https://memstate.ai) — a structured, versioned memory system for AI agents.

Use this skill when the Memstate MCP plugin is unavailable or when you want direct REST API access.

## What it does

- **Store facts** at hierarchical keypaths (`config.port = 8080`)
- **Ingest markdown** summaries — AI extracts keypaths automatically
- **Recall memories** by project, keypath, or semantic search
- **View history** — every change is versioned, nothing is lost
- **Manage projects** — create, browse, and delete project namespaces

## Quick Start

```bash
# Install via ClawHub
npx clawhub@latest install memstate-ai/memstate-ai

# Or clone directly
git clone https://github.com/memstate-ai/memstate-skill.git ~/.skills/memstate-ai
```

Set your API key:
```bash
export MEMSTATE_API_KEY="your_api_key_here"
# Get your key at https://memstate.ai/dashboard
```

## Usage

### Store a fact (keypath = value)
```bash
python3 scripts/memstate_set.py \
  --project "myapp" \
  --keypath "database.engine" \
  --value "PostgreSQL 16" \
  --category "decision"
```

### Ingest a markdown summary
```bash
python3 scripts/memstate_remember.py \
  --project "myapp" \
  --content "## Architecture\n- Backend: FastAPI\n- DB: PostgreSQL 16\n- Auth: JWT" \
  --source "agent"
```

### Recall memories
```bash
# Semantic search
python3 scripts/memstate_search.py --project "myapp" --query "how is auth configured"

# Browse project tree
python3 scripts/memstate_get.py --project "myapp"

# Get specific subtree
python3 scripts/memstate_get.py --project "myapp" --keypath "database" --include-content
```

### View history
```bash
python3 scripts/memstate_history.py --project "myapp" --keypath "database.engine"
```

### Delete memories
```bash
python3 scripts/memstate_delete.py --project "myapp" --keypath "config.old_setting"
python3 scripts/memstate_delete_project.py --project "old-project"
```

## Scripts

| Script | Purpose | Sync/Async |
|---|---|---|
| `memstate_set.py` | Store one keypath = value | Sync |
| `memstate_remember.py` | Ingest markdown, AI extracts keypaths | Async (~15s) |
| `memstate_get.py` | Browse projects, trees, subtrees, time-travel by revision | Sync |
| `memstate_search.py` | Semantic search by meaning | Sync |
| `memstate_history.py` | View version history | Sync |
| `memstate_delete.py` | Soft-delete a keypath | Sync |
| `memstate_delete_project.py` | Soft-delete an entire project | Sync |

## Validation

All 13 test cases pass against the live Memstate API:

```
✅ memstate_set: create, auto-version, second keypath
✅ memstate_get: list projects, project tree, subtree, time-travel (at_revision)
✅ memstate_search: semantic search
✅ memstate_history: by keypath
✅ memstate_remember: async markdown ingestion
✅ memstate_delete: soft-delete keypath
✅ memstate_delete_project: cleanup
```

Run the validation suite:
```bash
python3 scripts/validate_via_mcp.py
```

## Resources

- **Memstate AI:** [https://memstate.ai](https://memstate.ai)
- **Documentation:** [https://memstate.ai/docs](https://memstate.ai/docs)
- **MCP Plugin:** [https://github.com/memstate-ai/memstate-mcp](https://github.com/memstate-ai/memstate-mcp)
- **Benchmark:** [https://github.com/memstate-ai/memstate-benchmark](https://github.com/memstate-ai/memstate-benchmark)
- **npm:** [@memstate/mcp](https://www.npmjs.com/package/@memstate/mcp)

## License

MIT
