from typing import Optional
from .server import call_tool


async def notion_get_teams(query: Optional[str] = None) -> str:
    """
    Retrieves a list of teams (teamspaces) in the current workspace.

    Args:
        query: Optional search query to filter teams by name (case-insensitive).

    Returns:
        Tool result as string
    """
    # Build arguments dict
    arguments = {}

    # Add optional params only if provided
    if query:
        arguments["query"] = query

    # Call the MCP tool
    return await call_tool("notion-get-teams", arguments)


# Test - run with: python ./servers/notion/notion_get_teams.py
if __name__ == "__main__":
    import asyncio

    async def test():
        print("Testing notion_get_teams...")
        print("Note: This requires Notion authentication via mcp-remote OAuth")
        print("Skipping actual test to avoid authentication requirements")
        print("✓ Tool file created successfully")

    asyncio.run(test())

