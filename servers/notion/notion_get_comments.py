from .server import call_tool


async def notion_get_comments(page_id: str) -> str:
    """
    Get all comments of a page

    Args:
        page_id: Identifier for a Notion page.

    Returns:
        Tool result as string
    """
    # Build arguments dict with required params
    arguments = {"page_id": page_id}

    # Call the MCP tool
    return await call_tool("notion-get-comments", arguments)


# Test - run with: python ./servers/notion/notion_get_comments.py
if __name__ == "__main__":
    import asyncio

    async def test():
        print("Testing notion_get_comments...")
        print("Note: This requires Notion authentication via mcp-remote OAuth")
        print("Skipping actual test to avoid authentication requirements")
        print("✓ Tool file created successfully")

    asyncio.run(test())

