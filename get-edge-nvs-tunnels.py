"""

Velocloud Orchestrator API - v1 
monitoring/getEnterpriseEdgeNvsTunnelStatus

Get NVS Tunnels status

Reference: https://developer.broadcom.com/xapis/velocloud-orchestrator-api/latest/

"""



import asyncio
import os
import json
from dotenv import load_dotenv
from velocloud_api import VeloCloudAPI
import datetime
import time
from urllib.parse import urlencode
from datetime import datetime, timedelta, timezone

load_dotenv()

async def fetch_enterprise_logical_id(api_client, enterprise_id):
    """
    Fetch the logical ID of an enterprise using API v1.
    """
    endpoint = "/portal/rest/enterprise/getEnterprise"
    payload = {"id": int(enterprise_id)} 
    response = await api_client.api_request("POST", endpoint, payload)

    if "logicalId" in response:
        return response["logicalId"]
    else:
        raise ValueError(f"Failed to fetch logical ID: {response}")
    
async def get_all_edges(api_client, enterprise_id):
    """
    Fetch all edges for a given enterprise using API v1 
    """
    print("Fetching all edges for the enterprise...")

    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "monitoring/getEnterpriseEdgeNvsTunnelStatus",
        "params": {
            "enterpriseId": int(enterprise_id),
            "with": ["site"]  
        }
    }
    
    endpoint = "/portal/"

    response = await api_client.api_request(
        method="POST",
        endpoint=endpoint,
        payload=payload
    )
    print (response)
    return response


async def get_edge_nvs_tunnel(api_client, enterprise_id):
    """
    Get Edge NVS Tunnels Status
    """

    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "monitoring/getEnterpriseEdgeNvsTunnelStatus",
        "params": {
            "enterpriseId": int(enterprise_id),
            "tag": "NVS_FROM_EDGE_TUNNEL"
        }
    }

    endpoint = "/portal/"

    response = await api_client.api_request(
        method="POST",
        endpoint=endpoint,
        payload=payload
    )

    print (response)

    return response


async def main():
    # Load configurations
    base_url = os.getenv("ORCHESTRATOR_URL")
    token = os.getenv("API_TOKEN")
    enterprise_id = os.getenv("ENTERPRISE_ID")

    if not base_url or not token:
        raise ValueError("Missing required environment variables (ORCHESTRATOR_URL, API_TOKEN).")

    # Initialize API client
    api_client = VeloCloudAPI(base_url, token)

    
    response = await get_edge_nvs_tunnel(api_client,  enterprise_id)
    
    if "error" in response:
        print(f"Encountered the following error: {response['error']}")
    else:
        print("Results:")
        print(json.dumps(response, indent=4))

if __name__ == "__main__":
    asyncio.run(main())
