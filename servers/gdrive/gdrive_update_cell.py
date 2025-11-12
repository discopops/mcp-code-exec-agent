from .server import call_tool


async def gdrive_update_cell(
    fileId: str,
    range: str,
    value: str
) -> str:
    """
    Update a cell value in a Google Spreadsheet

    Args:
        fileId: ID of the spreadsheet
        range: Cell range in A1 notation (e.g. 'Sheet1!A1')
        value: New cell value

    Returns:
        Tool result as string
    """
    # Build arguments dict with required params
    arguments = {
        "fileId": fileId,
        "range": range,
        "value": value
    }

    # Call the MCP tool
    return await call_tool("gsheets_update_cell", arguments)


# Test - run with: python ./servers/gdrive/gdrive_update_cell.py
if __name__ == "__main__":
    import asyncio

    async def test():
        print("Testing gdrive_update_cell...")
        print("Note: This requires Google Drive authentication")
        print("Skipping actual test to avoid modifying user's spreadsheets")
        print("✓ Tool file created successfully")

    asyncio.run(test())

