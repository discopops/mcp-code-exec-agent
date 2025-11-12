from typing import Optional, Dict, Any, List
from .server import call_tool


async def notion_create_database(
    properties: Dict[str, Any],
    parent: Optional[Dict[str, Any]] = None,
    title: Optional[List[Any]] = None,
    description: Optional[List[Any]] = None
) -> str:
    """
    Creates a new Notion database with the specified properties schema.

    Args:
        properties: The property schema of the new database. If no title property is provided, one will be automatically added.
        parent: The parent under which to create the new database. If omitted, the database will be created as a private page at the workspace level.
        title: The title of the new database, as a rich text object.
        description: The description of the new database, as a rich text object.

    Returns:
        Tool result as string
    """
    # Build arguments dict with required params
    arguments = {"properties": properties}

    # Add optional params only if provided
    if parent:
        arguments["parent"] = parent
    if title:
        arguments["title"] = title
    if description:
        arguments["description"] = description

    # Call the MCP tool
    return await call_tool("notion-create-database", arguments)


# Test - run with: python ./servers/notion/notion_create_database.py
if __name__ == "__main__":
    import asyncio

    async def test():
        print("Testing notion_create_database...")
        print("Note: This requires Notion authentication via mcp-remote OAuth")
        print("Skipping actual test to avoid creating test databases in user's Notion")
        print("✓ Tool file created successfully")

    asyncio.run(test())

