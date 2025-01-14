"""

Velocloud Remote Diagnostics Websocket API - ARP Table Dump
"test": "IKE_CHILDSA"

Get IKE Phase 2 details for all tunnels on edge

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

async def run_arp_diagnostics(api_client, edge_logical_id, peer_ip):
    """
    Get All IKE_CHILDSA stats for edge
    """
    print("Running IKE_CHILDSA diagnostics...")

    
    response = await api_client.websocket_request(
        action="runDiagnostics",
        data={
            "logicalId": "01d7f9ad-d0e4-421b-9cc2-f1193cecad33",
            "resformat": "JSON",
            "test": "IKE_SA",
            "parameters": {
                "peer_ip": "51.0.0.253"
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
    
    edge_logical_id="01d7f9ad-d0e4-421b-9cc2-f1193cecad33"
    peer_ip= ""
    
    response =  await run_arp_diagnostics(api_client, edge_logical_id, peer_ip)

    if "error" in response:
        print(f"Encountered the following error: {response['error']}")
    else:
        print(json.dumps(response, indent=4))

if __name__ == "__main__":
    asyncio.run(main())
