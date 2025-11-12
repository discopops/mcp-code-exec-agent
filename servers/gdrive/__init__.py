"""
Google Drive MCP Tools

Progressive disclosure pattern - import only what you need.
See: https://www.anthropic.com/engineering/code-execution-with-mcp
"""

# Server management
from .server import get_server, ensure_connected, call_tool

# Individual tools
from .gdrive_search import gdrive_search
from .gdrive_read_file import gdrive_read_file
from .gdrive_update_cell import gdrive_update_cell
from .gdrive_read_sheet import gdrive_read_sheet

__all__ = [
    # Server
    "get_server",
    "ensure_connected",
    "call_tool",
    # Tools
    "gdrive_search",
    "gdrive_read_file",
    "gdrive_update_cell",
    "gdrive_read_sheet",
]

