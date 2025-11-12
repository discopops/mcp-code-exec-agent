from typing import Optional, List, Dict, Any
from .server import call_tool


async def notion_create_pages(
    pages: List[Dict[str, Any]],
    parent: Optional[Dict[str, Any]] = None
) -> str:
    """
    Creates one or more Notion pages, with the specified properties and content.

    Args:
        pages: The pages to create.
        parent: The parent under which the new pages will be created. This can be a page (page_id), a database page (database_id), or a data source/collection under a database (data_source_id). If omitted, the new pages will be created as private pages at the workspace level. Use data_source_id when you have a collection:// URL from the fetch tool.

    Returns:
        Tool result as string
    """
    # Build arguments dict with required params
    arguments = {"pages": pages}

    # Add optional params only if provided
    if parent:
        arguments["parent"] = parent

    # Call the MCP tool
    return await call_tool("notion-create-pages", arguments)


# Test - run with: python ./servers/notion/notion_create_pages.py
if __name__ == "__main__":
    import asyncio

    async def test():
        print("Testing notion_create_pages...")
        print("Note: This requires Notion authentication via mcp-remote OAuth")
        print("Skipping actual test to avoid creating test pages in user's Notion")
        print("✓ Tool file created successfully")

    asyncio.run(test())

