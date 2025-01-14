"""

Velocloud Orchestrator API - v1 
enterprise/getEnterpriseEdges

Get edges for the enterprise, where you can get edgeId, edge seria, edge name, edge logical id and more

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
    
async def get_all_edges(api_client, enterprise_id):
    """
    Fetch all edges for a given enterprise using API v1 
    """
    print("Fetching all edges for the enterprise...")

    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "enterprise/getEnterpriseEdges",
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

    # Get All Edges for the Enterprise
    response = await get_all_edges(api_client, enterprise_id)

    
    for edge in response["result"]:
        print(f'edge_id: {edge["id"]}, edge_name: {edge["name"]}, edge_logical_id: {edge["logicalId"]}')
    '''
    if "error" in response:
        print(f"Encountered the following error: {response['error']}")
    else:
        print("\nFull output:")
        print(json.dumps(response["result"], indent=4))
    '''
if __name__ == "__main__":
    asyncio.run(main())
