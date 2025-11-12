from typing import Optional, List
from .server import call_tool


async def gdrive_read_sheet(
    spreadsheetId: str,
    ranges: Optional[List[str]] = None,
    sheetId: Optional[int] = None
) -> str:
    """
    Read data from a Google Spreadsheet with flexible options for ranges and formatting

    Args:
        spreadsheetId: The ID of the spreadsheet to read
        ranges: Optional array of A1 notation ranges like ['Sheet1!A1:B10']. If not provided, reads entire sheet.
        sheetId: Optional specific sheet ID to read. If not provided with ranges, reads first sheet.

    Returns:
        Tool result as string
    """
    # Build arguments dict with required params
    arguments = {"spreadsheetId": spreadsheetId}

    # Add optional params only if provided
    if ranges:
        arguments["ranges"] = ranges
    if sheetId is not None:
        arguments["sheetId"] = sheetId

    # Call the MCP tool
    return await call_tool("gsheets_read", arguments)


# Test - run with: python ./servers/gdrive/gdrive_read_sheet.py
if __name__ == "__main__":
    import asyncio

    async def test():
        print("Testing gdrive_read_sheet...")
        print("Note: This requires Google Drive authentication")
        print("Skipping actual test to avoid authentication requirements")
        print("✓ Tool file created successfully")

    asyncio.run(test())

