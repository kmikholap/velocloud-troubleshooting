"""

Retrive all enterprises from the Velocloud Orchestrator using operator level token
Iterate over each enetrprise and get top 10 events in the specified timeframe

Reference: https://developer.broadcom.com/xapis/velocloud-orchestrator-api/latest/

"""


import asyncio
import os
import json
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from collections import Counter
from velocloud_api import VeloCloudAPI

import time
from urllib.parse import urlencode

load_dotenv()

def log_message(message):
    print(f"[{datetime.now().isoformat()}] {message}")

async def get_enterprises(api_client):
    """
    Get all enterprises
    """
    log_message("Authenticating and retrieving enterprises...")
    payload = {
        "jsonrpc": "2.0",
        "method": "enterprise/getEnterprisesWithProperty",
        "id": 6,
        "params": {
            "name": "vco.enterprise.edgeImageManagement.enable",
            "value": "true"
        }
    }
    endpoint = "/portal/"
    response = await api_client.api_request("POST", endpoint, payload)

    if "error" in response:
        log_message(f"Authentication or data retrieval failed: {response['error']}")
        raise SystemExit("Exiting due to authentication failure.")

    log_message("Successfully retrieved enterprises.")
    return response.get("result", [])

async def get_events(api_client, enterprise_id, hours):
    """
    Get events per enterprise for a specified timeframe.
    """
    log_message(f"Getting events for enterprise ID: {enterprise_id}...")
    now = datetime.now(timezone.utc)
    start_time = now - timedelta(hours=hours)
    payload = {
        "jsonrpc": "2.0",
        "method": "event/getEnterpriseEventsList",
        "id": 24,
        "params": {
            "sortBy": [
                {"attribute": "eventTime", "type": "DESC"}
            ],
            "enterpriseId": int(enterprise_id),
            "interval": {
                "type": "custom",
                "start": int(start_time.timestamp() * 1000),
                "end": int(now.timestamp() * 1000)
            },
            "limit": 50,
            "_filterSpec": True
        }
    }
    endpoint = "/portal/"
    response = await api_client.api_request("POST", endpoint, payload)

    if "error" in response:
        log_message(f"Error fetching events for enterprise ID {enterprise_id}: {response['error']}")
        return []

    return response.get("result", {}).get("data", [])

async def process_enterprise_events(api_client, hours, output_file):
    """
    Process events and find the top 10.
    """
    enterprises = await get_enterprises(api_client)

    with open(output_file, "w") as file:
        for enterprise in enterprises:
            enterprise_id = enterprise["id"]
            enterprise_name = enterprise.get("name", "Unknown")
            log_message(f"Processing events for enterprise: {enterprise_name} (ID: {enterprise_id})")
            file.write(f"\nProcessing events for enterprise: {enterprise_name} (ID: {enterprise_id})\n")

            events = await get_events(api_client, enterprise_id, hours)
            if not events:
                log_message(f"No events found for enterprise ID {enterprise_id}.")
                file.write(" - No events found in the specified timeframe.\n")
                continue

            event_counter = Counter(event["event"] for event in events)
            top_events = event_counter.most_common(10)

            # Write events to file
            for event_code, count in top_events:
                file.write(f" - Event Code: {event_code}, Count: {count}\n")

async def main():
    # Load vars
    base_url = os.getenv("ORCHESTRATOR_URL")
    token = os.getenv("API_TOKEN")

    output_file = "top_ent_events.txt"
    hours = 168  # Specify how far back you want to go in hours
    
    if not base_url or not token:
        raise ValueError("Missing required environment variables (ORCHESTRATOR_URL, API_TOKEN).")
    
    api_client = VeloCloudAPI(base_url, token)

    try:
        await process_enterprise_events(api_client, hours, output_file)
        log_message(f"Wrote output to {output_file}")
    except SystemExit as e:
        log_message(str(e))
    except Exception as e:
        log_message(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())
