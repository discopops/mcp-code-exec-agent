"""Google Drive MCP Server Configuration"""
from agents.mcp import MCPServerStdio
from typing import Optional
import os
import json

# Singleton server instance
_server: Optional[MCPServerStdio] = None
_connected: bool = False

def _ensure_oauth_keys():
    """Ensure OAuth keys file exists from environment variable"""
    creds_json = os.getenv('GDRIVE_CREDENTIALS_JSON')
    if not creds_json:
        return  # Keys might already exist or using individual env vars
    
    creds_dir = os.getenv('GDRIVE_CREDS_DIR', './mnt/mcp-creds')
    os.makedirs(creds_dir, exist_ok=True)
    creds_file = os.path.join(creds_dir, 'gcp-oauth.keys.json')
    
    # Only create if it doesn't exist
    if not os.path.exists(creds_file):
        try:
            creds_data = json.loads(creds_json)
            with open(creds_file, 'w') as f:
                json.dump(creds_data, f, indent=2)
        except Exception:
            pass  # Silently fail, let MCP handle the error

def get_server() -> MCPServerStdio:
    """Get the Google Drive MCP server instance (singleton)"""
    global _server
    if _server is None:
        # Ensure OAuth keys exist from environment variable
        _ensure_oauth_keys()
        
        _server = MCPServerStdio(
            name="GoogleDrive",
            params={
                "command": "npx",
                "args": ["-y", "@isaacphi/mcp-gdrive"],
                "env": {
                    "GDRIVE_CREDS_DIR": os.getenv("GDRIVE_CREDS_DIR", "./mnt/mcp-creds")
                }
            },
            cache_tools_list=True,
            client_session_timeout_seconds=60  # Increased for OAuth flow
        )
    return _server

async def ensure_connected() -> MCPServerStdio:
    """Ensure the server is connected, connect if not"""
    global _connected
    server = get_server()
    
    if not _connected:
        await server.connect()
        _connected = True
    
    return server

async def call_tool(tool_name: str, arguments: dict):
    """Call a tool on the MCP server with the given arguments"""
    server = await ensure_connected()
    
    # Get the session
    session = getattr(server, 'session', None) or getattr(server, '_client_session', None)
    if not session:
        raise RuntimeError("Could not access MCP session")
    
    # Call the tool
    result = await session.call_tool(name=tool_name, arguments=arguments)
    
    # Extract content from result
    if hasattr(result, 'content'):
        content = result.content
        if isinstance(content, list) and len(content) > 0:
            return content[0].text if hasattr(content[0], 'text') else str(content[0])
        return str(content)
    
    return result

# Tool discovery - run with: python ./servers/gdrive/server.py
if __name__ == "__main__":
    import asyncio
    
    async def discover_tools():
        print("Discovering tools from Google Drive MCP server...")
        server = await ensure_connected()
        
        session = getattr(server, 'session', None) or getattr(server, '_client_session', None)
        if session:
            tools_result = await session.list_tools()
            tools = tools_result.tools if hasattr(tools_result, 'tools') else []
            
            print(f"\nFound {len(tools)} tools:\n")
            for tool in tools:
                print(f"Tool: {tool.name}")
                print(f"  Description: {tool.description}")
                if hasattr(tool, 'inputSchema') and 'properties' in tool.inputSchema:
                    print(f"  Parameters:")
                    schema = tool.inputSchema
                    for param_name, param_info in schema['properties'].items():
                        param_type = param_info.get('type', 'any')
                        param_desc = param_info.get('description', '')
                        required = param_name in schema.get('required', [])
                        print(f"    - {param_name}: {param_type} {'(required)' if required else '(optional)'}")
                        if param_desc:
                            print(f"      {param_desc}")
                print()
    
    asyncio.run(discover_tools())

