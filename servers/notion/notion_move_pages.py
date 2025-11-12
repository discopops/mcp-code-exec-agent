from typing import List, Any
from .server import call_tool


async def notion_move_pages(
    page_or_database_ids: List[str],
    new_parent: Any
) -> str:
    """
    Move one or more Notion pages or databases to a new parent.

    Args:
        page_or_database_ids: An array of up to 100 page or database IDs to move. IDs are v4 UUIDs and can be supplied with or without dashes (e.g. extracted from a <page> or <database> URL given by the "search" or "fetch" tool). Data Sources under Databases can't be moved individually.
        new_parent: The new parent under which the pages will be moved. This can be a page, the workspace, a database, or a specific data source under a database when there are multiple. Moving pages to the workspace level adds them as private pages and should rarely be used.

    Returns:
        Tool result as string
    """
    # Build arguments dict with required params
    arguments = {
        "page_or_database_ids": page_or_database_ids,
        "new_parent": new_parent
    }

    # Call the MCP tool
    return await call_tool("notion-move-pages", arguments)


# Test - run with: python ./servers/notion/notion_move_pages.py
if __name__ == "__main__":
    import asyncio

    async def test():
        print("Testing notion_move_pages...")
        print("Note: This requires Notion authentication via mcp-remote OAuth")
        print("Skipping actual test to avoid moving user's Notion pages")
        print("✓ Tool file created successfully")

    asyncio.run(test())

