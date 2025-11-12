from typing import Dict, Any, List
from .server import call_tool


async def notion_create_comment(
    parent: Dict[str, Any],
    rich_text: List[Any]
) -> str:
    """
    Add a comment to a page

    Args:
        parent: The parent of the comment. This must be a page.
        rich_text: An array of rich text objects that represent the content of the comment.

    Returns:
        Tool result as string
    """
    # Build arguments dict with required params
    arguments = {
        "parent": parent,
        "rich_text": rich_text
    }

    # Call the MCP tool
    return await call_tool("notion-create-comment", arguments)


# Test - run with: python ./servers/notion/notion_create_comment.py
if __name__ == "__main__":
    import asyncio

    async def test():
        print("Testing notion_create_comment...")
        print("Note: This requires Notion authentication via mcp-remote OAuth")
        print("Skipping actual test to avoid creating comments in user's Notion")
        print("✓ Tool file created successfully")

    asyncio.run(test())

