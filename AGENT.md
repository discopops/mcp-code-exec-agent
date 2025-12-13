# Sales Ops Agent - Code Execution with MCP

This repository implements Anthropic's "Code Execution with MCP" pattern, enabling AI agents to dynamically generate and execute Python code for interacting with external services like Google Drive and Notion. This approach drastically reduces token consumption (up to 88%) by loading tools on-demand and fostering the creation of reusable "skills" for common tasks.

**Key Technologies/Frameworks**:
Python, IPythonInterpreter, PersistentShellTool, Anthropic Code Execution with MCP Pattern, Agency Swarm, Google Drive API, Notion API.

**Main Features**:
Dynamic code generation and execution, on-demand tool loading, skill creation and reuse for task optimization, comprehensive integration with Google Drive (file/sheet operations), and Notion (page/database management, comments, user interactions).

**Architectural Patterns**:
Agent-based system, code generation/execution, modular MCP servers as code APIs, dynamic tool discovery via filesystem, skill-based learning for efficiency, and persistent storage for skills and credentials. This promotes autonomous, token-efficient, and scalable agent operations.
