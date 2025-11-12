from typing import Optional
from .server import call_tool


async def notion_get_users(
    query: Optional[str] = None,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None
) -> str:
    """
    Retrieves a list of users in the current workspace.

    Args:
        query: Optional search query to filter users by name or email (case-insensitive).
        start_cursor: Cursor for pagination. Use the next_cursor value from the previous response to get the next page.
        page_size: Number of users to return per page (default: 100, max: 100).

    Returns:
        Tool result as string
    """
    # Build arguments dict
    arguments = {}

    # Add optional params only if provided
    if query:
        arguments["query"] = query
    if start_cursor:
        arguments["start_cursor"] = start_cursor
    if page_size:
        arguments["page_size"] = page_size

    # Call the MCP tool
    return await call_tool("notion-get-users", arguments)


# Test - run with: python ./servers/notion/notion_get_users.py
if __name__ == "__main__":
    import asyncio

    async def test():
        print("Testing notion_get_users...")
        print("Note: This requires Notion authentication via mcp-remote OAuth")
        print("Skipping actual test to avoid authentication requirements")
        print("✓ Tool file created successfully")

    asyncio.run(test())

