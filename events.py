"""

Velocloud Orchestrator API - v2
/api/sdwan/v2/enterprises/{logical_id}/events

Get All Enterprise Events for a specified amount of time, ie 12 hours, 24 hours etc

Reference: https://developer.broadcom.com/xapis/vmware-sd-wan-orchestration-api-v2/latest/

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

async def fetch_enterprise_events_timeframe(api_client, logical_id, hours):
    """
    Fetch enterprise events using API v2 within a specific time frame.
    """
   
    now = int(datetime.datetime.now(datetime.timezone.utc).timestamp() * 1000)  # Current time in milliseconds
    start_time = now - (hours * 3600 * 1000)  # Timeframe start in milliseconds

   
    endpoint = f"/api/sdwan/v2/enterprises/{logical_id}/events"
    params = {
        "start": start_time,
        "end": now
    }


    response = await api_client.api_request("GET", endpoint, params)
    return response


async def main():
   
    base_url = os.getenv("ORCHESTRATOR_URL")
    token = os.getenv("API_TOKEN")
    enterprise_id = os.getenv("ENTERPRISE_ID")

    if not base_url or not token:
        raise ValueError("Missing required environment variables (ORCHESTRATOR_URL, API_TOKEN).")


    api_client = VeloCloudAPI(base_url, token)

    # Get LogicalID using APIv1
    print("Fetching logical ID for enterprise...")
    logical_id = await fetch_enterprise_logical_id(api_client, enterprise_id)
    print(f"Fetched Logical ID: {logical_id}")

    # Get enterprise events for a specific timeframe (in hr) 
    timeframe = 12
    print(f"Fetching enterprise events for the last {timeframe} hours...")
    response = await fetch_enterprise_events_timeframe(api_client, logical_id, timeframe)
    
    if "error" in response:
        print(f"Encountered the following error: {response['error']}")
    else:
        print("Results:")
        print(json.dumps(response, indent=4))

if __name__ == "__main__":
    asyncio.run(main())
