from .server import call_tool


async def notion_duplicate_page(page_id: str) -> str:
    """
    Duplicate a Notion page.

    Args:
        page_id: The ID of the page to duplicate. This is a v4 UUID, with or without dashes, and can be parsed from a Notion page URL.

    Returns:
        Tool result as string
    """
    # Build arguments dict with required params
    arguments = {"page_id": page_id}

    # Call the MCP tool
    return await call_tool("notion-duplicate-page", arguments)


# Test - run with: python ./servers/notion/notion_duplicate_page.py
if __name__ == "__main__":
    import asyncio

    async def test():
        print("Testing notion_duplicate_page...")
        print("Note: This requires Notion authentication via mcp-remote OAuth")
        print("Skipping actual test to avoid duplicating user's Notion pages")
        print("✓ Tool file created successfully")

    asyncio.run(test())

