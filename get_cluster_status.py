"""

Velocloud Orchestrator API - v1

monitoring/getEnterpriseEdgeClusterStatus
Get all edge clusters

Reference: Reference: https://developer.broadcom.com/xapis/velocloud-orchestrator-api/latest/
"""

import asyncio
import os
import json
from dotenv import load_dotenv
from velocloud_api import VeloCloudAPI
import datetime
import time
from urllib.parse import urlencode
from datetime import datetime, timedelta


load_dotenv()



async def get_edge_clusters(api_client, enterprise_id):
    """
    Get All CLusters in the interprise
    """

    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "monitoring/getEnterpriseEdgeClusterStatus",
        "params": {
            "enterpriseId": int(enterprise_id),
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
   
    base_url = os.getenv("ORCHESTRATOR_URL")
    token = os.getenv("API_TOKEN")
    enterprise_id = os.getenv("ENTERPRISE_ID")

    if not base_url or not token:
        raise ValueError("Missing required environment variables (ORCHESTRATOR_URL, API_TOKEN).")

    api_client = VeloCloudAPI(base_url, token)
    
    response = await get_edge_clusters(api_client, enterprise_id)

    print(json.dumps(response, indent=4))

if __name__ == "__main__":
    asyncio.run(main())
