"""

Velocloud Orchestrator API - v1
/metrics/getEdgeAppMetrics

Get flow metric aggregate data by application per interval, ie 12 hours, 24 hours etc

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
from datetime import datetime, timedelta


load_dotenv()



async def get_edge_app_metrics_timeframe(api_client, enterprise_id, edge_id, hours):
    """
    Get edge Application metrics per specified timeframe in hours
    """
   
    # Get the current timestamp in milliseconds
    now = datetime.now()
    now_ms = int(now.timestamp() * 1000)

    # Calculate the start time (12 hours before now)
    start_time = now - timedelta(hours=hours)
    start_time_ms = int(start_time.timestamp() * 1000)

    endpoint = "/portal/rest/metrics/getEdgeAppMetrics"

    payload = {
        "enterpriseId": int(enterprise_id),   
        "edgeId": edge_id,
        "interval": {
            "start": start_time_ms,
            "end": now_ms
        },
        "resolveApplicationNames": True
    }  
    
    response = await api_client.api_request("POST", endpoint, payload)
   
    return response
    
    

async def main():
   
    base_url = os.getenv("ORCHESTRATOR_URL")
    token = os.getenv("API_TOKEN")
    enterprise_id = os.getenv("ENTERPRISE_ID")

    if not base_url or not token:
        raise ValueError("Missing required environment variables (ORCHESTRATOR_URL, API_TOKEN).")


    api_client = VeloCloudAPI(base_url, token)

    
    edge_id = 1
    timeframe = 168

    print(f"Getting app metrics for the last {timeframe} hours...")
    response = await get_edge_app_metrics_timeframe(api_client, enterprise_id, edge_id,timeframe)
    
   
    print(json.dumps(response, indent=4))

if __name__ == "__main__":
    asyncio.run(main())
