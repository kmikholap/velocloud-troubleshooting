"""

Velocloud Orchestrator API - v1 
/metrics/getEdgeStatusSeries

Get edge time series (5m interval) metrics for edge stats including , cpu, memory, tunnel, flow count and more

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


async def get_edge_status_series(api_client, edges, enterprise_id, hours):
    """
    Get Edge series
    """
    print("Running edge metrics  ...")

    end_time = datetime.now(timezone.utc)
    start_time = end_time - timedelta(hours=hours)

    # Format the times to ISO8601 
    end_iso = end_time.isoformat(timespec='milliseconds').replace('+00:00', 'Z')
    start_iso = start_time.isoformat(timespec='milliseconds').replace('+00:00', 'Z')


    results = []
    for edge in edges['result']:
        edge_id = edge.get("id")
        if not edge_id:
            continue

        print(f"Running metrics pull for {edge_id}...")

        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "metrics/getEdgeStatusSeries",
            "params": {
                "enterpriseId": int(enterprise_id),
                "edgeId": int(edge_id),
                "role": "ACTIVE",
                "interval": {
                    "end": end_iso,
                    "start": start_iso
                },
                "metrics": [
                    "tunnelCount",
                    #"cpuPct"
                    #"memoryPct",
                    #"flowCount",
                    #"handoffQueueDrops"
                ]
            }
        }

        endpoint = "/portal/"

        response = await api_client.api_request(
            method="POST",
            endpoint=endpoint,
            payload=payload
        )

        results.append({"edge": int(edge_id), "result": response["result"]})

    return results




async def main():
    # Load configurations
    base_url = os.getenv("ORCHESTRATOR_URL")
    token = os.getenv("API_TOKEN")
    enterprise_id = os.getenv("ENTERPRISE_ID")

    if not base_url or not token:
        raise ValueError("Missing required environment variables (ORCHESTRATOR_URL, API_TOKEN).")

    # Initialize API client
    api_client = VeloCloudAPI(base_url, token)

    # Get LogicalID using APIv1
    print("Fetching logical ID for enterprise...")
    logical_id = await fetch_enterprise_logical_id(api_client, enterprise_id)
    print(f"Fetched Logical ID: {logical_id}")

    # Get All Edges for the Enterprise
    edges= await get_all_edges(api_client, enterprise_id)
    

    # Get edge metrics for a specific timeframe (in hr) 
    
    timeframe = 24
    response = await get_edge_status_series(api_client, edges, enterprise_id, timeframe)
    
    if "error" in response:
        print(f"Encountered the following error: {response['error']}")
    else:
        print("Results:")
        print(json.dumps(response, indent=4))

if __name__ == "__main__":
    asyncio.run(main())
