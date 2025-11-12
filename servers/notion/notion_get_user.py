from typing import Dict, Any
from .server import call_tool


async def notion_get_user(path: Dict[str, Any]) -> str:
    """
    Retrieve a user

    Args:
        path: Path object

    Returns:
        Tool result as string
    """
    # Build arguments dict with required params
    arguments = {"path": path}

    # Call the MCP tool
    return await call_tool("notion-get-user", arguments)


# Test - run with: python ./servers/notion/notion_get_user.py
if __name__ == "__main__":
    import asyncio

    async def test():
        print("Testing notion_get_user...")
        print("Note: This requires Notion authentication via mcp-remote OAuth")
        print("Skipping actual test to avoid authentication requirements")
        print("✓ Tool file created successfully")

    asyncio.run(test())

