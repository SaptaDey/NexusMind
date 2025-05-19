#!/usr/bin/env python3
"""
Helper script to set up the NexusMind MCP connection with Claude Desktop.
This script:
1. Tests if the NexusMind server is running
2. Displays instructions for connecting with Claude Desktop
"""

import requests
import json
import os
import sys
import time

# Configuration
SERVER_URL = "http://localhost:8000"
MCP_ENDPOINT = f"{SERVER_URL}/mcp"
HEALTH_ENDPOINT = f"{SERVER_URL}/health"
CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config", "claude_mcp_config.json")

def check_health():
    """Check if the NexusMind server is running by testing the health endpoint."""
    try:
        response = requests.get(HEALTH_ENDPOINT)
        if response.status_code == 200:
            health_data = response.json()
            print(f"✅ Server is running: Status {health_data['status']}, Version {health_data['version']}")
            return True
        else:
            print(f"❌ Server returned non-200 status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error connecting to server: {e}")
        return False

def test_mcp_initialize():
    """Test the MCP endpoint by sending an initialize request."""
    init_payload = {
        "jsonrpc": "2.0",
        "id": "setup-script-1",
        "method": "initialize",
        "params": {
            "client_info": {
                "client_name": "NexusMind Setup Script"
            },
            "process_id": 12345
        }
    }
    
    try:
        response = requests.post(
            MCP_ENDPOINT,
            json=init_payload,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            result = response.json()
            if "result" in result and result["result"]:
                print(f"✅ MCP endpoint initialized successfully")
                print(f"   Server name: {result['result'].get('server_name', 'N/A')}")
                print(f"   Server version: {result['result'].get('server_version', 'N/A')}")
                print(f"   MCP version: {result['result'].get('mcp_version', 'N/A')}")
                return True
            else:
                print(f"❌ MCP endpoint returned an error: {json.dumps(result.get('error', {}), indent=2)}")
                return False
        else:
            print(f"❌ MCP endpoint returned status code: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error testing MCP endpoint: {e}")
        return False

def check_config_file():
    """Check if the MCP configuration file exists and is valid."""
    if not os.path.exists(CONFIG_FILE):
        print(f"❌ MCP configuration file not found: {CONFIG_FILE}")
        return False
    
    try:
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
        
        # Validate essential fields
        if (
            "connection" in config and
            "endpoint" in config["connection"] and
            config["connection"]["endpoint"] == MCP_ENDPOINT
        ):
            print(f"✅ MCP configuration file is valid")
            return True
        else:
            print(f"⚠️  MCP configuration file has issues:")
            if "connection" not in config:
                print("   Missing 'connection' field")
            elif "endpoint" not in config["connection"]:
                print("   Missing 'endpoint' field in connection")
            elif config["connection"]["endpoint"] != MCP_ENDPOINT:
                print(f"   Endpoint mismatch: {config['connection']['endpoint']} vs {MCP_ENDPOINT}")
            return False
    except json.JSONDecodeError:
        print(f"❌ MCP configuration file is not valid JSON")
        return False
    except Exception as e:
        print(f"❌ Error checking MCP configuration: {e}")
        return False

def display_instructions():
    """Display instructions for connecting with Claude Desktop."""
    print("\n" + "=" * 60)
    print("CLAUDE DESKTOP CONNECTION INSTRUCTIONS")
    print("=" * 60)
    print("\n1. Open Claude Desktop")
    print("2. Go to Settings (gear icon)")
    print("3. Navigate to Tools or Integrations")
    print("4. Add a new Tool/Integration")
    print("5. Import the MCP configuration file from:")
    print(f"   {os.path.abspath(CONFIG_FILE)}")
    print("\nAlternative manual setup:")
    print("- Name: NexusMind MCP Integration")
    print("- Description: Scientific reasoning with Graph of Thoughts")
    print(f"- Endpoint: {MCP_ENDPOINT}")
    print("- Method: POST")
    print("- Headers: Content-Type: application/json")
    print("\nFor complete instructions, see:")
    print("docs/claude_desktop_integration.md")
    print("\n" + "=" * 60)

def main():
    print("\n=== NexusMind MCP Setup ===\n")
    
    # Step 1: Check if server is running
    print("Step 1: Checking if NexusMind server is running...")
    if not check_health():
        print("\n⚠️  WARNING: Server not running. Please start the server and try again.")
        print("   Docker command: docker-compose up -d")
        sys.exit(1)
    
    # Step 2: Test MCP endpoint
    print("\nStep 2: Testing MCP endpoint...")
    if not test_mcp_initialize():
        print("\n⚠️  WARNING: MCP endpoint not working properly.")
        print("   Please check the server logs for errors.")
    
    # Step 3: Check config file
    print("\nStep 3: Checking MCP configuration file...")
    check_config_file()
    
    # Step 4: Display instructions
    print("\nStep 4: Connection instructions...")
    display_instructions()
    
    print("\nSetup complete! You can now connect Claude Desktop to the NexusMind server.")
    print("Test the integration by asking a scientific reasoning question.")

if __name__ == "__main__":
    main()
