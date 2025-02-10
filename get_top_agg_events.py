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
import re
import time
from urllib.parse import urlencode
from collections import defaultdict
import pprint
import argparse
import sys
# This file store all the credentials for logging to the VCO in the format of
# api_tokens = {
#     "vco12-usvi1.velocloud.net": "your_token_here",
#     # ... other VCO tokens
# }
from vco_tokens import api_tokens

load_dotenv()

sleep_time = 10
min_edges = 25
hours = 24 * 7  # Specify how far back you want to go in hours

def log_message(message):
    print(f"[{datetime.now().isoformat()}] {message}")

async def get_enterprises(api_client):
    """
    Get all the edges and parse the number of connected edges
    """
    log_message("Fetching all edges...")
    payload = {
        "jsonrpc": "2.0",
        "method": "monitoring/getEnterpriseEdgeLinkStatus",
        "id": 1,
        "params": { "links": False }
    }
    endpoint = "/portal/"
    response = await api_client.api_request("POST", endpoint, payload)

    if "error" in response:
        log_message(f"Error fetching edges: {response['error']}")
        return []

    log_message("Successfully retrieve edges for all enterprises")

    # Now we need to parse this output
    enterprises = defaultdict(lambda: defaultdict(str))
    for edge in response["result"]:
        ent_name = edge["enterpriseName"]
        edge_state = edge["edgeState"]
        if not enterprises[ent_name]:
            enterprises[ent_name]["id"] = edge["enterpriseId"]
        enterprises[ent_name][edge_state] = enterprises[ent_name].get(edge_state, 0) + 1

    # Filter out to just enterprises that meet these criteria
    # No. of connected edges >= 10
    # Enterprise name has lab or demo
    regx_pat = '[ \\-]([Ll][Aa][Bb]|[Dd][Ee][Mm][Oo])'
    return_value = []
    for ent_name in enterprises:
        connected_edge = enterprises[ent_name].get("CONNECTED", 0)
        if connected_edge < min_edges or bool(re.search(regx_pat, ent_name)):
            continue
        return_value.append(
            {
                "name": ent_name,
                "id": enterprises[ent_name]["id"],
                "connected_edges": connected_edge,
            }
        )
    return return_value

async def get_n_events(api_client, enterprise_id, start_time, end_time, limit=500, next_page_link=None):
    """
    Get events per enterprise for a specified timeframe.
    """
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
                "end": int(end_time.timestamp() * 1000)
            },
            "limit": limit,
            "filters": {
                "and": [ 
                    {
                        "field": "severity",
                        "operator": "in",
                        "value": ["ERROR", "CRITICAL", "ALERT", "EMERGENCY", "WARNING", "INFO"]
                    }
                ],
            },
            "_filterSpec": True
        }  
    }
    if next_page_link is not None:
        payload["params"]["nextPageLink"] = next_page_link
    
    endpoint = "/portal/"
    response = await api_client.api_request("POST", endpoint, payload)

    if "error" in response:
        log_message(f"Error fetching events for enterprise ID {enterprise_id}: {response['error']}")
        return {}

    return response.get("result", {})

async def get_events(api_client, enterprise_id, hours):
    """
    Get events per enterprise for a specified timeframe.
    """
    max = 20000
    event_count = 0
    # log_message(f"Getting events for enterprise ID: {enterprise_id}...")
    now = datetime.now(timezone.utc)
    start_time = now - timedelta(hours=hours)
    next_page_link = None
    limit = 500
    events = []

    # First get the total event count
    payload = {
        "jsonrpc": "2.0",
        "method": "event/getEnterpriseEventsList",
        "id": 24,
        "params": {
            "enterpriseId": int(enterprise_id),
            "interval": {
                "type": "custom",
                "start": int(start_time.timestamp() * 1000),
                "end": int(now.timestamp() * 1000)
            },
            "filters": {
                "and": [ 
                    {
                        "field": "severity",
                        "operator": "in",
                        "value": ["ERROR", "CRITICAL", "ALERT", "EMERGENCY", "WARNING", "INFO"]
                    }
                ],
            },
            "_count": True
        }  
    }
    endpoint = "/portal/"
    response = await api_client.api_request("POST", endpoint, payload)

    if "error" in response:
        log_message(f"Error getting num of events for enterprise ID {enterprise_id}: {response['error']}")
        return events, 0
    
    total_event_count = response.get("result", {}).get("count", 0)
    log_message(f"Getting events for enterprise ID: {enterprise_id}...total event count: {total_event_count}")

    # Get the first output
    while event_count < max:
        output = await get_n_events(api_client, enterprise_id, start_time, now, limit=limit, next_page_link=next_page_link)
        # Now parse this output
        next_page_link = output.get("metaData", {}).get("nextPageLink", None)
        events += output.get("data", [])
        event_count += len(output.get("data", []))
        log_message(f"Fetching up to {limit} events from enterprise id {enterprise_id}, current event count {event_count}...")
        await asyncio.sleep(sleep_time)
        if not next_page_link:
            break

    return events, total_event_count

async def get_aggregate_ent_events(api_client, hours):
    """
    Get events per enterprise for a specified timeframe.
    """
    log_message(f"Getting aggregate events for all enterprises...")
    now = datetime.now(timezone.utc)
    start_time = now - timedelta(hours=hours)
    limit = 500
    next_page_link = None

    payload = {
        "jsonrpc": "2.0",
        "method": "monitoring/getAggregateEnterpriseEvents",
        "id": 24,
        "params": {
            "interval": {
                "start": int(start_time.timestamp() * 1000),
                "end": int(now.timestamp() * 1000)
            },
            "limit": limit,
            "rules": [ 
                {
                    "field": "severity",
                    "op": "in",
                    "values": ["ERROR", "CRITICAL", "ALERT", "EMERGENCY", "WARNING", "INFO"]
                }
            ]
        }  
    }
    if next_page_link is not None:
        payload["params"]["nextPageLink"] = next_page_link
    
    endpoint = "/portal/"
    response = await api_client.api_request("POST", endpoint, payload)

    if "error" in response:
        log_message(f"Error fetching aggregate events: {response['error']}")
        return {}

    return response.get("result", {})    

async def process_enterprise_events(api_client, hours, output_file):
    """
    Process events and find the top 10.
    """

    # aggregated_events = await get_aggregate_ent_events(api_client, hours)
    enterprises = await get_enterprises(api_client)
    # enterprises += await get_enterprises(api_client, "false")

    await asyncio.sleep(sleep_time)

    with open(output_file, "w") as file:
        for enterprise in enterprises:
            enterprise_id = enterprise["id"]
            enterprise_name = enterprise.get("name", "Unknown")
            connected_edges = enterprise.get("connected_edges", 0)
            events, total_event_count = await get_events(api_client, enterprise_id, hours)
            log_message(f"Processing events for enterprise: {enterprise_name} (ID: {enterprise_id}) Connected Edges: {connected_edges}, total event count: {total_event_count}")
            file.write(f"\nProcessing events for enterprise: {enterprise_name} (ID: {enterprise_id}) Connected Edges: {connected_edges}, total event count: {total_event_count}\n")
            if not events:
                log_message(f"No events found for enterprise ID {enterprise_id}.")
                file.write(" - No events found in the specified timeframe.\n")
                continue

            event_counter = Counter(f'{event["severity"]}_{event["event"]}' for event in events)
            top_events = event_counter.most_common(30)

            # Write events to file
            for event_code, count in top_events:
                file.write(f" - Event Code: {event_code}, Count: {count}\n")
            
            await asyncio.sleep(sleep_time * 2)

    return

async def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--vcos', nargs='+', default=api_tokens.keys(), help='List of VCOs')
    args = parser.parse_args()
    vcos = args.vcos
    base_urls = [x for x in api_tokens.keys() if x in vcos]
    log_message(f"List of VCOs: {base_urls}")
    for base_url in base_urls:
        token = api_tokens[base_url]
        output_file = f"{base_url}-top_ent_events.txt"
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
