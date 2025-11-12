from agency_swarm import Agent
import sys
from pathlib import Path
from openai.types.shared import Reasoning
from agents import ModelSettings

# Add parent directory to path to import server configurations
parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))

from servers.gdrive.server import get_server as get_gdrive_server
from servers.notion.server import get_server as get_notion_server

# Get the MCP server instances
gdrive_server = get_gdrive_server()
notion_server = get_notion_server()

sales_ops_direct_mcp = Agent(
    name="SalesOpsDirectMCP",
    description="Sales operations agent with direct MCP integration for advanced capabilities.",
    instructions="./instructions.md",
    tools_folder="./tools",
    files_folder="./files",
    model="gpt-5",
    mcp_servers=[gdrive_server, notion_server],
    model_settings=ModelSettings(
        reasoning=Reasoning(
            effort="medium",
            summary="auto",
        ),
    ),
)


if __name__ == "__main__":
    import asyncio

    async def test_mcp_integration():
        """Test MCP server integration"""
        print("Testing MCP server integration for SalesOpsDirectMCP agent...\n")
        
        # Test Google Drive MCP Server
        print("=" * 60)
        print("Google Drive MCP Server")
        print("=" * 60)
        try:
            await gdrive_server.connect()
            tools_result = await gdrive_server.list_tools()
            tools = tools_result.tools if hasattr(tools_result, 'tools') else tools_result
            print(f"✓ Connected successfully")
            print(f"✓ Found {len(tools)} tools:\n")
            for tool in tools:
                print(f"  • {tool.name}")
                if hasattr(tool, 'description'):
                    print(f"    {tool.description}")
        except Exception as e:
            print(f"✗ Error connecting to Google Drive MCP: {e}")
        
        print("\n" + "=" * 60)
        print("Notion MCP Server")
        print("=" * 60)
        try:
            await notion_server.connect()
            tools_result = await notion_server.list_tools()
            tools = tools_result.tools if hasattr(tools_result, 'tools') else tools_result
            print(f"✓ Connected successfully")
            print(f"✓ Found {len(tools)} tools:\n")
            for tool in tools:
                print(f"  • {tool.name}")
                if hasattr(tool, 'description'):
                    print(f"    {tool.description}")
        except Exception as e:
            print(f"✗ Error connecting to Notion MCP: {e}")
        
        print("\n" + "=" * 60)
        print("Agent Response Test")
        print("=" * 60)
        try:
            result = await sales_ops_direct_mcp.get_response(
                "List all the tools you have access to from Google Drive and Notion."
            )
            print(f"\n{result.final_output}")
        except Exception as e:
            print(f"✗ Error getting agent response: {e}")

    asyncio.run(test_mcp_integration())

