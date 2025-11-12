from typing import Optional, Dict, Any
from .server import call_tool


async def notion_search(
    query: str,
    query_type: Optional[str] = None,
    data_source_url: Optional[str] = None,
    page_url: Optional[str] = None,
    teamspace_id: Optional[str] = None,
    filters: Optional[Dict[str, Any]] = None
) -> str:
    """
    Perform a search over Notion workspace and connected sources.

    Args:
        query: Semantic search query over your entire Notion workspace and connected sources (Slack, Google Drive, Github, Jira, Microsoft Teams, Sharepoint, OneDrive, or Linear). For best results, don't provide more than one question per tool call. Use a separate "search" tool call for each search you want to perform. Alternatively, the query can be a substring or keyword to find users by matching against their name or email address. For example: "john" or "john@example.com"
        query_type: Optional query type
        data_source_url: Optionally, provide the URL of a Data source to search. This will perform a semantic search over the pages in the Data Source. Note: must be a Data Source, not a Database. <data-source> tags are part of the Notion flavored Markdown format returned by tools like fetch. The full spec is available in the create-pages tool description.
        page_url: Optionally, provide the URL or ID of a page to search within. This will perform a semantic search over the content within and under the specified page. Accepts either a full page URL (e.g. https://notion.so/workspace/Page-Title-1234567890) or just the page ID (UUIDv4) with or without dashes.
        teamspace_id: Optionally, provide the ID of a teamspace to restrict search results to. This will perform a search over content within the specified teamspace only. Accepts the teamspace ID (UUIDv4) with or without dashes.
        filters: Optionally provide filters to apply to the search results. Only valid when query_type is 'internal'.

    Returns:
        Tool result as string
    """
    # Build arguments dict with required params
    arguments = {"query": query}

    # Add optional params only if provided
    if query_type:
        arguments["query_type"] = query_type
    if data_source_url:
        arguments["data_source_url"] = data_source_url
    if page_url:
        arguments["page_url"] = page_url
    if teamspace_id:
        arguments["teamspace_id"] = teamspace_id
    if filters:
        arguments["filters"] = filters

    # Call the MCP tool
    return await call_tool("notion-search", arguments)


# Test - run with: python ./servers/notion/notion_search.py
if __name__ == "__main__":
    import asyncio

    async def test():
        print("Testing notion_search...")
        print("Note: This requires Notion authentication via mcp-remote OAuth")
        print("Skipping actual test to avoid authentication requirements")
        print("✓ Tool file created successfully")

    asyncio.run(test())

