"""

Velocloud Orchestrator API - v1

Get flow metric aggregate data by application (app_id) per interval, ie 12 hours, 24 hours etc

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



async def get_edge_device_metrics_timeframe(api_client, enterprise_id, edge_id, app_id,  hours):
    """
    Get edge device Application metrics per specified timeframe in hours
    """
   

    now = datetime.now()
    now_ms = int(now.timestamp() * 1000)
    start_time = now - timedelta(hours=hours)
    start_time_ms = int(start_time.timestamp() * 1000)

    endpoint = "/portal/rest/metrics/getEdgeDeviceMetrics"

    payload = {
        "enterpriseId": int(enterprise_id),   
        "edgeId": edge_id,
        "interval": {
            "start": start_time_ms,
            "end": now_ms
        },
        "filter": {
            "rules": [
                {
                  "field": "application",
                  "op": "=",
                  "values": [app_id],
                }
            ]
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
    app_id ="32" # DNS App ID, get it from /metrics/getEdgeAppMetrics
    timeframe = 168 # 7 days

    print(f"Getting per app device metrics for the last {timeframe} hours...")
    response = await get_edge_device_metrics_timeframe(api_client, enterprise_id, edge_id, app_id, timeframe)
    
   
    print(json.dumps(response, indent=4))

if __name__ == "__main__":
    asyncio.run(main())
