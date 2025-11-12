from typing import Any
from .server import call_tool


async def notion_update_page(data: Any) -> str:
    """
    Update a Notion page's properties or content.

    Args:
        data: The data required for updating a page

    Returns:
        Tool result as string
    """
    # Build arguments dict with required params
    arguments = {"data": data}

    # Call the MCP tool
    return await call_tool("notion-update-page", arguments)


# Test - run with: python ./servers/notion/notion_update_page.py
if __name__ == "__main__":
    import asyncio

    async def test():
        print("Testing notion_update_page...")
        print("Note: This requires Notion authentication via mcp-remote OAuth")
        print("Skipping actual test to avoid modifying user's Notion pages")
        print("✓ Tool file created successfully")

    asyncio.run(test())

