from typing import Optional
from .server import call_tool


async def gdrive_search(
    query: str,
    pageToken: Optional[str] = None,
    pageSize: Optional[int] = None
) -> str:
    """
    Search for files in Google Drive

    Args:
        query: Search query
        pageToken: Token for the next page of results
        pageSize: Number of results per page (max 100)

    Returns:
        Tool result as string
    """
    # Build arguments dict with required params
    arguments = {"query": query}

    # Add optional params only if provided
    if pageToken:
        arguments["pageToken"] = pageToken
    if pageSize:
        arguments["pageSize"] = pageSize

    # Call the MCP tool
    return await call_tool("gdrive_search", arguments)


# Test - run with: python ./servers/gdrive/gdrive_search.py
if __name__ == "__main__":
    import asyncio

    async def test():
        print("Testing gdrive_search...")
        print("Note: This requires Google Drive authentication")
        print("Skipping actual test to avoid authentication requirements")
        print("✓ Tool file created successfully")

    asyncio.run(test())

