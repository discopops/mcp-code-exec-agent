from .server import call_tool


async def gdrive_read_file(fileId: str) -> str:
    """
    Read contents of a file from Google Drive

    Args:
        fileId: ID of the file to read

    Returns:
        Tool result as string
    """
    # Build arguments dict with required params
    arguments = {"fileId": fileId}

    # Call the MCP tool
    return await call_tool("gdrive_read_file", arguments)


# Test - run with: python ./servers/gdrive/gdrive_read_file.py
if __name__ == "__main__":
    import asyncio

    async def test():
        print("Testing gdrive_read_file...")
        print("Note: This requires Google Drive authentication")
        print("Skipping actual test to avoid authentication requirements")
        print("✓ Tool file created successfully")

    asyncio.run(test())

