from .server import call_tool


async def notion_get_self() -> str:
    """
    Retrieve your token's bot user

    Returns:
        Tool result as string
    """
    # Build arguments dict
    arguments = {}

    # Call the MCP tool
    return await call_tool("notion-get-self", arguments)


# Test - run with: python ./servers/notion/notion_get_self.py
if __name__ == "__main__":
    import asyncio

    async def test():
        print("Testing notion_get_self...")
        print("Note: This requires Notion authentication via mcp-remote OAuth")
        print("Skipping actual test to avoid authentication requirements")
        print("✓ Tool file created successfully")

    asyncio.run(test())

