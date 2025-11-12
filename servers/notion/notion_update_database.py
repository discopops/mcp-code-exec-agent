from typing import Optional, List, Dict, Any
from .server import call_tool


async def notion_update_database(
    database_id: str,
    title: Optional[List[Any]] = None,
    description: Optional[List[Any]] = None,
    properties: Optional[Dict[str, Any]] = None,
    is_inline: Optional[bool] = None,
    in_trash: Optional[bool] = None
) -> str:
    """
    Update a Notion database's properties, name, description, or other attributes.

    Args:
        database_id: The ID of the database to update. This is a UUID v4, with or without dashes, and can be parsed from a database URL.
        title: The new title of the database, as a rich text object, if you want to update it.
        description: The new description of the database, as a rich text object, if you want to update it.
        properties: Updates to make to the database's schema. Use null to remove a property, or provide the `name` only to rename a property.
        is_inline: Optional is_inline flag
        in_trash: Optional in_trash flag

    Returns:
        Tool result as string
    """
    # Build arguments dict with required params
    arguments = {"database_id": database_id}

    # Add optional params only if provided
    if title:
        arguments["title"] = title
    if description:
        arguments["description"] = description
    if properties:
        arguments["properties"] = properties
    if is_inline is not None:
        arguments["is_inline"] = is_inline
    if in_trash is not None:
        arguments["in_trash"] = in_trash

    # Call the MCP tool
    return await call_tool("notion-update-database", arguments)


# Test - run with: python ./servers/notion/notion_update_database.py
if __name__ == "__main__":
    import asyncio

    async def test():
        print("Testing notion_update_database...")
        print("Note: This requires Notion authentication via mcp-remote OAuth")
        print("Skipping actual test to avoid modifying user's Notion databases")
        print("✓ Tool file created successfully")

    asyncio.run(test())

