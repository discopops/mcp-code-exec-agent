from typing import Optional
from .server import call_tool


async def notion_list_agents(query: Optional[str] = None) -> str:
    """
    Retrieves a list of all custom agents (workflows) that the authenticated user has access to.

    Args:
        query: Optional search query to filter agents by name or description (case-insensitive).

    Returns:
        Tool result as string
    """
    # Build arguments dict
    arguments = {}

    # Add optional params only if provided
    if query:
        arguments["query"] = query

    # Call the MCP tool
    return await call_tool("notion-list-agents", arguments)


# Test - run with: python ./servers/notion/notion_list_agents.py
if __name__ == "__main__":
    import asyncio

    async def test():
        print("Testing notion_list_agents...")
        print("Note: This requires Notion authentication via mcp-remote OAuth")
        print("Skipping actual test to avoid authentication requirements")
        print("✓ Tool file created successfully")

    asyncio.run(test())

