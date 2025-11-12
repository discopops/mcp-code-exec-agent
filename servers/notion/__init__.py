"""
Notion MCP Tools

Progressive disclosure pattern - import only what you need.
See: https://www.anthropic.com/engineering/code-execution-with-mcp
"""

# Server management
from .server import get_server, ensure_connected, call_tool

# Individual tools
from .notion_search import notion_search
from .notion_fetch import notion_fetch
from .notion_create_pages import notion_create_pages
from .notion_update_page import notion_update_page
from .notion_move_pages import notion_move_pages
from .notion_duplicate_page import notion_duplicate_page
from .notion_create_database import notion_create_database
from .notion_update_database import notion_update_database
from .notion_create_comment import notion_create_comment
from .notion_get_comments import notion_get_comments
from .notion_get_teams import notion_get_teams
from .notion_get_users import notion_get_users
from .notion_list_agents import notion_list_agents
from .notion_get_self import notion_get_self
from .notion_get_user import notion_get_user

__all__ = [
    # Server
    "get_server",
    "ensure_connected",
    "call_tool",
    # Tools
    "notion_search",
    "notion_fetch",
    "notion_create_pages",
    "notion_update_page",
    "notion_move_pages",
    "notion_duplicate_page",
    "notion_create_database",
    "notion_update_database",
    "notion_create_comment",
    "notion_get_comments",
    "notion_get_teams",
    "notion_get_users",
    "notion_list_agents",
    "notion_get_self",
    "notion_get_user",
]

