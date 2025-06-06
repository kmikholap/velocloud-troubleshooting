"""

Velocloud Remote Diagnostics Websocket API 
"test": "SYSTEM_INFORMATION"

Reference: https://developer.broadcom.com/xapis/vmware-sd-wan-remote-diagnostics-websocket-api/latest/

"""

import asyncio
import os
import json
from dotenv import load_dotenv
from velocloud_api import VeloCloudAPI
import datetime
import time
from urllib.parse import urlencode

# Load environment variables
load_dotenv()

async def fetch_enterprise_logical_id(api_client, enterprise_id):
    """
    Fetch the logical ID of an enterprise using API v1.
    """
    endpoint = "/portal/rest/enterprise/getEnterprise"
    payload = {"id": int(enterprise_id)}  # Numeric enterprise ID
    response = await api_client.api_request("POST", endpoint, payload)

    if "logicalId" in response:
        return response["logicalId"]
    else:
        raise ValueError(f"Failed to fetch logical ID: {response}")


async def get_all_edges(api_client, enterprise_id):
    """
    Fetch all edges for a given enterprise using API v1 with JSON-RPC format.
    """
    print("Fetching all edges for the enterprise...")

    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "enterprise/getEnterpriseEdges",
        "params": {
            "enterpriseId": int(enterprise_id),
            "with": ["site"]  # Optional: Include site details if needed
        }
    }
    endpoint = "/portal/"

    response = await api_client.api_request(
        method="POST",
        endpoint=endpoint,
        payload=payload
    )

    return response

async def system_information(api_client, edges):
    """
    Run System Infos diagnostics on all edges
    """
    print("Running Interface diagnostics...")

    results = []
    for edge in edges['result']:
        logical_id = edge.get("logicalId")
        if not logical_id:
            continue

        print(f"Running diagnostics for edge {logical_id}...")
        response = await api_client.websocket_request(
            action="runDiagnostics",
            data={
                "logicalId": logical_id,
                "resformat": "JSON",
                "test": "SYSTEM_INFORMATION",
            }
        )

        if "action" in response and response["action"] == "runDiagnostics":
            result = response.get("data", {}).get("results", {})
            if "output" in result:
                try:
                    result["output"] = json.loads(result["output"])
                except json.JSONDecodeError:
                    print(f"Failed to decode output for edge {logical_id}")
            results.append({"logical_id": logical_id, "result": result})
        else:
            results.append({"logical_id": logical_id, "error": response.get("error", "Unexpected response format")})
        
    return results

async def main():
    base_url = os.getenv("ORCHESTRATOR_URL")
    token = os.getenv("API_TOKEN")
    enterprise_id = os.getenv("ENTERPRISE_ID")

    if not base_url or not token:
        raise ValueError("Missing required environment variables (ORCHESTRATOR_URL, API_TOKEN).")

    api_client = VeloCloudAPI(base_url, token)

    print("Fetching logical ID for enterprise...")
    logical_id = await fetch_enterprise_logical_id(api_client, enterprise_id)
    print(f"Fetched Logical ID: {logical_id}")

    
    # Get All Edges for the Enterprise
    edges= await get_all_edges(api_client, enterprise_id)

    # System info request
    response =  await system_information(api_client, edges)

    if "error" in response:
        print(f"Encountered the following error: {response['error']}")
    else:
        print("Results:")
        print(json.dumps(response, indent=4))

if __name__ == "__main__":
    asyncio.run(main())
