# Sales Ops Agent - MCP Code Execution Pattern

**98% reduction in token consumption while giving agents more autonomy and flexibility.**

> ⚠️ **IMPORTANT: Keep this repository PRIVATE**
>
> This implementation stores OAuth credentials in `./mnt/mcp-creds/` which are currently committed to the repository. Proper OAuth flow for MCP servers is coming soon to the Agencii platform. Until then, ensure your repository visibility is set to **private** to protect your credentials.

This implementation follows Anthropic's [Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) pattern, where agents write code to interact with MCP servers instead of making direct tool calls. The agent discovers tools by exploring the filesystem and loads only what it needs for each task.

## Why This Approach?

**Traditional MCP (Direct Tool Calls):**

- Loads all 19 tool definitions upfront (~150K tokens)
- Every intermediate result flows through model context
- Example: Copying a transcript consumes 32K tokens

**Code Execution Pattern:**

- Loads tools on-demand from filesystem (~2K tokens)
- Processes data in execution environment
- Same task consumes 4K tokens with skills, 12K without

## Architecture

```
sales_ops agent
├── IPythonInterpreter (code execution)
├── PersistentShellTool (file discovery)
└── MCP Servers (as code APIs)
    ├── servers/notion/ (15 tools)
    │   ├── search.py
    │   ├── fetch.py
    │   └── ... (other tools)
    └── servers/gdrive/ (4 tools)
        ├── search.py
        ├── read_file.py
        ├── read_sheet.py
        └── update_cell.py
```

## Quick Start

### 1. Clone Repository

```bash
git clone <your-repo>
cd code-exec-agent
```

### 2. Setup Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Credentials

Add to `.env`:

```bash
OPENAI_API_KEY=your-openai-key

# Google Drive (required)
GDRIVE_CREDENTIALS_JSON={"installed":{"client_id":"...","client_secret":"...","redirect_uris":["http://localhost"]}}

# Notion (uses OAuth via mcp-remote - auto-configured)
```

**Getting Google Drive Credentials:**

1. Create Google Cloud project
2. Enable Google Drive API, Google Sheets API, Google Docs API
3. Create OAuth Client ID for "Desktop App"
4. Download JSON and add to `GDRIVE_CREDENTIALS_JSON`

### 4. Authenticate Google Drive

```bash
npx @isaacphi/mcp-gdrive
# Follow OAuth flow in browser
# Press Ctrl+C after "Setting up automatic token refresh"
```

### 5. Test the Agent

```bash
python agency.py
```

## Example Test Task

**Task:** Add transcript from Google Doc to Notion page

```
Add this transcript from this Google doc https://docs.google.com/document/d/YOUR_DOC_ID
to this Notion page https://www.notion.so/YOUR_PAGE_ID
```

**What Happens:**

1. Agent checks `./mnt/skills/` for existing skill
2. If not found, reads only needed tools:
   - `servers/gdrive/read_file.py`
   - `servers/notion/update_page.py`
3. Writes code in IPythonInterpreter:

```python
from servers.gdrive import read_file
from servers.notion import update_page

# Read transcript (stays in execution environment)
transcript = await read_file(fileId="YOUR_DOC_ID")

# Update Notion page
await update_page(data={
    "page_id": "YOUR_PAGE_ID",
    "command": "replace_content",
    "new_str": transcript
})
```

4. Suggests saving as reusable skill
5. Next time: uses skill directly (4K tokens vs 12K)

## Convert a Traditional MCP Agent to this Pattern with Cursor

Follow this step-by-step workflow using Cursor's AI commands:

### Step 1: Create Agent MVP (If not already created)

```
Create a sales_ops agent with 2 built-in tools: IPythonInterpreter and PersistentShellTool
```

**Why these tools:**

- `IPythonInterpreter` - Executes code with top-level await
- `PersistentShellTool` - Discovers files and reads tool definitions

### Step 2: Add MCP Servers Using Code Execution Pattern

```
/mcp-code-exec

Add the following mcp servers to sales_ops agent:
https://developers.notion.com/docs/get-started-with-mcp
https://github.com/isaacphi/mcp-gdrive
```

**What this does:**

- Creates `servers/notion/` with 15 tool files
- Creates `servers/gdrive/` with 4 tool files
- Each tool is a Python file with async function
- Auto-creates `server.py` for connection management
- Tests server connections

### Step 3: Write Agent Instructions

```
/write-instructions @sales_ops.py

Main role: Performing operational tasks for the team
Business goal: Improve efficiency
Process:
1. Discover skills in ./mnt/skills folder
2. Use skill if it matches task
3. If no skills found, read ONLY necessary tool files
4. Import and combine tools in IPythonInterpreter
5. Suggest new skills to be added

Keep these instructions short. Don't add mcp usage examples or don't list all mcps. Agent should discover them autonomously.

Agent should also minimize token consumption by performing as few tool calls as possible and only reading the necessary tool files to complete the task.

Output: Summary + skill suggestions
```

**Key workflow points:**

- **Skills-first approach** - Always check `./mnt/skills/` first
- **Progressive disclosure** - Only read tools you need
- **Self-improvement** - Create reusable skills over time
- **Minimize token consumption** - Agent shouldn't read too many files

### Step 4: Handle Authentication

If you see authentication errors:

```
I added secrets, please retest google drive tools make sure each tool is production ready
```

Then authenticate:

```bash
npx @isaacphi/mcp-gdrive
```

### Step 5: Test and Deploy

```bash
# Test locally
python agency.py

# Deploy to Agency Swarm platform
git push origin main
# Go to platform.agency-swarm.ai
# Create new agency from repo
# Add environment variables
```

## How It Works

### Traditional Direct MCP (Comparison Agent)

```
User: Add transcript to Notion

Agent → MCP: gdrive.read_file(docId)
MCP → Agent: [Full 50KB transcript in context]

Agent → MCP: notion.update_page(pageId, transcript)
        [Agent rewrites full 50KB transcript again]

Result: 32,000 tokens consumed
```

### Code Execution Pattern (This Implementation)

```
User: Add transcript to Notion

Agent → Shell: ls ./mnt/skills/
Agent → Shell: cat servers/gdrive/read_file.py

Agent → IPython:
    from servers.gdrive import read_file
    from servers.notion import update_page
    transcript = await read_file(fileId="...")
    await update_page(data={...})

Result: 12,000 tokens (first time), 4,000 tokens (with skill)
```

### Progressive Disclosure

Instead of loading all 19 tools upfront:

```
# Traditional: All tools loaded immediately
✗ 150K tokens - Full definitions for all 19 tools in context

# Code Execution: Load on demand
✓ 2K tokens - List directory to see available tools
✓ Read only the 2 files needed for current task
```

### Skills System

Agent builds its own library of reusable functions:

```
./mnt/skills/
├── copy_gdrive_to_notion.py
├── export_sheet_to_csv.py
└── search_and_email_results.py
```

Skills persist across chat sessions. Each completed task is an opportunity to create a new skill.

## Performance Comparison

**Test Task:** Copy Google Doc transcript to Notion page

| Approach       | First Run  | With Skill | Reduction |
| -------------- | ---------- | ---------- | --------- |
| Direct MCP     | 32K tokens | 32K tokens | -         |
| Code Execution | 12K tokens | 4K tokens  | **88%**   |

## When to Use This Approach

✅ **Use Code Execution Pattern for:**

- Operations agents (data sync, reporting)
- Research agents (gather, analyze, summarize)
- Analytics agents (query, transform, visualize)
- Agents with 10+ tools
- Tasks with large data processing

❌ **Use Traditional MCP for:**

- Simple customer support (3-5 tools)
- Single-purpose agents
- Tasks requiring immediate consistency
- When infrastructure overhead isn't acceptable

## Agent Workflow

The agent follows this process for every task:

```
1. Check Skills
   └─ ls ./mnt/skills/
   └─ If match found → Execute skill → Done

2. Identify Tools Needed
   └─ Based on task: Notion? Drive? Both?

3. Read ONLY Necessary Tools
   └─ cat servers/notion/fetch.py
   └─ cat servers/gdrive/read_file.py
   └─ DO NOT read server.py or other files

4. Combine Tools in Code
   └─ Write Python code in IPythonInterpreter
   └─ Use await directly (top-level await enabled)

5. Suggest New Skill
   └─ Analyze workflow
   └─ Propose reusable function
   └─ Save to ./mnt/skills/
```

## Available Tools

### Notion MCP (15 tools)

**Content Operations:**

- `search()` - Semantic search across workspace
- `fetch()` - Get page/database details
- `create_pages()` - Create new pages
- `update_page()` - Update properties/content
- `move_pages()` - Move to new parent
- `duplicate_page()` - Duplicate page

**Database Operations:**

- `create_database()` - Create with schema
- `update_database()` - Update schema

**Comments:**

- `create_comment()` - Add comment
- `get_comments()` - Get all comments

**Workspace:**

- `get_teams()` - List teams
- `get_users()` - List users
- `list_agents()` - List custom agents
- `get_self()` - Get bot info
- `get_user()` - Get specific user

### Google Drive MCP (4 tools)

**Drive:**

- `search()` - Search files
- `read_file()` - Read contents

**Sheets:**

- `read_sheet()` - Read spreadsheet
- `update_cell()` - Update cell value

## Project Structure

```
code-exec-agent/
├── sales_ops/                    # Main agent
│   ├── sales_ops.py             # Agent configuration
│   ├── instructions.md          # Agent prompt (key to performance)
│   └── tools/                   # Built-in tools (empty - uses framework)
├── servers/                     # MCP servers as code
│   ├── notion/
│   │   ├── server.py           # Connection management
│   │   ├── __init__.py         # Exports all tools
│   │   ├── search.py           # Individual tool
│   │   └── ... (15 tools)
│   └── gdrive/
│       ├── server.py
│       ├── __init__.py
│       └── ... (4 tools)
├── mnt/
│   ├── skills/                  # Agent-created reusable functions
│   └── mcp-creds/              # OAuth tokens (auto-managed)
├── agency.py                    # Entry point
├── .env                         # Credentials
└── requirements.txt
```

## Troubleshooting

### Agent reads too many files

**Problem:** Agent reads server.py, README.md, etc.

**Solution:** Update instructions.md:

```markdown
**DO NOT** read any other tool, readme, or server files to avoid extra token consumption.
Only read what you need for the specific task.
```

### OAuth/Authentication errors

**Problem:** OAuth/Authentication are not working after deployment.

**Solution:**

1. Ensure all OAuth tokens are saved to `./mnt/mcp-creds/`
2. Ensure persistent storage is enabled under "Agency" tab

or

1. Trigg OAuth flow again locally
2. Commit and deploy to Agencii.ai
3. Test in another chat

### Agent doesn't use skills

**Problem:** Persistent storage is not enabled so skills are not saved.

**Solution:**

1. Open your agency on Agencii.ai
2. Enable storage under "Agency" tab
3. Wait for build to complete
4. Tell your agent to save the skill
5. Test in another chat

## Deployment

### Option 1: Local Development

```bash
python agency.py
```

### Option 2: Agency Swarm Platform

1. Push to GitHub (private repo)
2. Go to https://agencii.ai
3. Create new agency from repo
4. Add environment variables
5. Deploy

**Platform Benefits:**

- Persistent `./mnt/` storage (skills preserved)
- Automatic scaling
- Built-in tracing & analytics
- No infrastructure management

## Performance Tips

1. **Write clear instructions** - Prompting is key for this pattern
2. **Build skills progressively** - Start simple, improve over time
3. **Use specific task descriptions** - Help agent identify needed tools
4. **Review traces** - Check platform dashboard for optimization opportunities
5. **Start with common workflows** - Build skill library for repeated tasks

## Production Readiness

**✅ Ready for production IF:**

- You have clear, well-tested instructions
- Tasks are operational (not simple Q&A)
- You monitor and optimize prompts
- You use skills for repeated workflows

**⚠️ Not recommended for:**

- Simple customer support (use direct MCP)
- Mission-critical real-time operations
- Tasks requiring <1s response time

## References

- [Anthropic: Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp)
- [Agency Swarm Documentation](https://agency-swarm.ai)
- [Notion MCP Server](https://developers.notion.com/docs/get-started-with-mcp)
- [Google Drive MCP Server](https://github.com/isaacphi/mcp-gdrive)

## Contributing

This is a reference implementation of the Code Execution Pattern. Improvements welcome:

1. Better prompting strategies
2. More efficient skill suggestions
3. Additional MCP server integrations
4. Performance optimizations

## License

MIT

---

**Built with [Agency Swarm](https://agency-swarm.ai) implementing [Anthropic's Code Execution Pattern](https://www.anthropic.com/engineering/code-execution-with-mcp)**
