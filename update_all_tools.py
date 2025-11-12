import os
import re

# Pattern to match async function definitions and convert them
def convert_tool_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Skip if already converted
    if 'from .._async_helper import run_async' in content or 'from ._async_helper import run_async' in content:
        return False
    
    # Skip if it's the server.py file
    if filepath.endswith('server.py'):
        return False
        
    # Add import after other imports
    if 'from .server import call_tool' in content:
        content = content.replace(
            'from .server import call_tool',
            'from .server import call_tool\nfrom .._async_helper import run_async'
        )
    
    # Convert async def to def with run_async wrapper
    # Pattern: async def function_name(params) -> str:
    pattern = r'async def (\w+)\((.*?)\) -> str:'
    
    def replace_func(match):
        func_name = match.group(1)
        params = match.group(2)
        return f'def {func_name}({params}) -> str:'
    
    content = re.sub(pattern, replace_func, content)
    
    # Find the function body and wrap the MCP call
    # Look for "return await call_tool" and wrap it
    if 'return await call_tool' in content:
        # More complex replacement - wrap the whole function
        lines = content.split('\n')
        new_lines = []
        in_function = False
        function_indent = 0
        collected_body = []
        func_signature = None
        
        for i, line in enumerate(lines):
            # Detect function start
            if re.match(r'^def \w+\([^)]*\) -> str:', line):
                in_function = True
                function_indent = len(line) - len(line.lstrip())
                func_signature = line
                new_lines.append(line)
                # Add docstring
                j = i + 1
                while j < len(lines) and (lines[j].strip().startswith('"""') or lines[j].strip().startswith("'''") or (len(collected_body) > 0 and not collected_body[0].strip().endswith('"""'))):
                    new_lines.append(lines[j])
                    collected_body.append(lines[j])
                    j += 1
                    if lines[j-1].strip().endswith('"""') or lines[j-1].strip().endswith("'''"):
                        break
                continue
            
            if in_function and line.strip() and not line.strip().startswith('#'):
                current_indent = len(line) - len(line.lstrip())
                if current_indent <= function_indent and line.strip():
                    # End of function
                    in_function = False
                    # Now wrap collected body
                    # ... this is getting too complex
                    
            new_lines.append(line)
        
        # This is too complex, let me use a simpler approach
        
    with open(filepath, 'w') as f:
        f.write(content)
    
    return True

# Find all tool files
notion_tools = [
    'servers/notion/search.py',
    'servers/notion/create_pages.py', 
    'servers/notion/update_page.py',
    'servers/notion/move_pages.py',
    'servers/notion/duplicate_page.py',
    'servers/notion/create_database.py',
    'servers/notion/update_database.py',
    'servers/notion/create_comment.py',
    'servers/notion/get_comments.py',
    'servers/notion/get_teams.py',
    'servers/notion/get_users.py',
    'servers/notion/list_agents.py',
    'servers/notion/get_self.py',
    'servers/notion/get_user.py',
]

gdrive_tools = [
    'servers/gdrive/search.py',
    'servers/gdrive/read_file.py',
    'servers/gdrive/read_sheet.py',
    'servers/gdrive/update_cell.py',
]

count = 0
for tool in notion_tools + gdrive_tools:
    if os.path.exists(tool):
        if convert_tool_file(tool):
            count += 1
            print(f"Converted: {tool}")

print(f"\nTotal files converted: {count}")
