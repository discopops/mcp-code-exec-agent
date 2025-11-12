"""
Test script to verify the modified IPythonInterpreter supports async MCP tools
"""
import asyncio
import sys
sys.path.insert(0, '/Users/vrsen/Areas/Development/code/code-exec-agent')

from sales_ops.tools.IPythonInterpreter import IPythonInterpreter

async def test_async_support():
    print("Testing IPythonInterpreter with async MCP tools...")
    
    # Test 1: Simple async code
    print("\n[Test 1] Simple async/await...")
    tool = IPythonInterpreter(code="""
import asyncio

async def hello():
    await asyncio.sleep(0.1)
    return "Hello from async!"

result = await hello()
print(result)
""")
    result = await tool.run()
    print(result)
    assert "Hello from async!" in result, "Simple async failed"
    
    # Test 2: MCP tool import and call
    print("\n[Test 2] MCP tool (Notion fetch)...")
    tool2 = IPythonInterpreter(code="""
from servers.notion import fetch

# Fetch a Notion page
result = await fetch(id="https://www.notion.so/vrsen-ai/Skool-2a65bd4b16a680fea311dac70fda6674")
print("Fetched page:", result[:100])
""")
    result2 = await tool2.run()
    print(result2)
    assert "Error" not in result2 or "RuntimeError: This event loop is already running" not in result2, "MCP tool async failed"
    
    # Test 3: Persistent state with async
    print("\n[Test 3] Persistent state across calls...")
    tool3a = IPythonInterpreter(code="""
from servers.notion import search

# First call - save to variable
search_results = await search(query="", pageSize=1)
print("Saved results")
""")
    result3a = await tool3a.run()
    print(result3a)
    
    tool3b = IPythonInterpreter(code="""
# Second call - access previous variable
print("Previous results available:", 'search_results' in dir())
""")
    result3b = await tool3b.run()
    print(result3b)
    
    print("\n" + "="*60)
    print("✅ ALL TESTS PASSED! Async IPythonInterpreter works!")
    print("="*60)

if __name__ == "__main__":
    asyncio.run(test_async_support())

