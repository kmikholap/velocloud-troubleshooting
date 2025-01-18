"""

Velocloud Remote Diagnostics Websocket API - ARP Table Dump
"test": "CLEAR_ARP"

Clear arp entries on the specified Interface of the edge

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

load_dotenv()

async def clear_arp_cache(api_client, edge_logical_id, interface):
    """
    Clear Arp on all edges using WebSocket.
    """
    print(f"Clearing arp for for edge {edge_logical_id}...")
    response = await api_client.websocket_request(
        action="runDiagnostics",
        data={
            "logicalId": edge_logical_id,
            "resformat": "JSON",
            "test": "CLEAR_ARP",
            "parameters": {
                "interface": interface
            }
        }
    )
        
    return response


async def main():
    base_url = os.getenv("ORCHESTRATOR_URL")
    token = os.getenv("API_TOKEN")
    enterprise_id = os.getenv("ENTERPRISE_ID")

    if not base_url or not token:
        raise ValueError("Missing required environment variables (ORCHESTRATOR_URL, API_TOKEN).")

    api_client = VeloCloudAPI(base_url, token)
    

    edge_logical_id="01d7f9ad-d0e4-421b-9cc2-f1193cecad33" # Get from enterprise/getEnterpriseEdges (example: get-enterprise-edges.py)
    interface ="GE4"


    # Clear Arp Websocket request
    response =  await clear_arp_cache(api_client, edge_logical_id, interface)

    if "error" in response:
        print(f"Encountered the following error: {response['error']}")
    else:
        print(json.dumps(response, indent=4))

if __name__ == "__main__":
    asyncio.run(main())
