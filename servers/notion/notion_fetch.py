from .server import call_tool


async def notion_fetch(id: str) -> str:
    """
    Retrieves details about a Notion entity (page or database) by URL or ID.

    Args:
        id: The ID or URL of the Notion page to fetch

    Returns:
        Tool result as string
    """
    # Build arguments dict with required params
    arguments = {"id": id}

    # Call the MCP tool
    return await call_tool("notion-fetch", arguments)


# Test - run with: python ./servers/notion/notion_fetch.py
if __name__ == "__main__":
    import asyncio

    async def test():
        print("Testing notion_fetch...")
        print("Note: This requires Notion authentication via mcp-remote OAuth")
        print("Skipping actual test to avoid authentication requirements")
        print("✓ Tool file created successfully")

    asyncio.run(test())

