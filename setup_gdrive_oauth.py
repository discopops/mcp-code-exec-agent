import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the credentials JSON from environment variable
credentials_json = os.getenv("GDRIVE_CREDENTIALS_JSON")
creds_dir = os.getenv("GDRIVE_CREDS_DIR", "./mnt/mcp-creds")

if not credentials_json:
    print("Error: GDRIVE_CREDENTIALS_JSON not found in .env file")
    exit(1)

# Parse the JSON
try:
    credentials = json.loads(credentials_json)
    print("✓ Successfully parsed credentials JSON")
except json.JSONDecodeError as e:
    print(f"Error: Invalid JSON in GDRIVE_CREDENTIALS_JSON: {e}")
    exit(1)

# Ensure the credentials directory exists
os.makedirs(creds_dir, exist_ok=True)

# Write the credentials to the file that Google Drive MCP expects
keys_file_path = os.path.join(creds_dir, "gcp-oauth.keys.json")
with open(keys_file_path, 'w') as f:
    json.dump(credentials, f, indent=2)

print(f"✓ OAuth keys file created at: {keys_file_path}")
print("\nYou can now authenticate by running:")
print("  npx @isaacphi/mcp-gdrive")
