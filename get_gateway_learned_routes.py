"""

Velocloud Orchestrator API - v1
Get routes learned on gateway from edge. If routes are present and reachable==true, tunnels are up

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


async def get_enterprise_logical_id(api_client, enterprise_id):
    """
    Fetch the logical ID of an enterprise using API v1.
    """
    endpoint = "/portal/rest/enterprise/getEnterprise"
    payload = {
        "id": int(enterprise_id)
    } 
    response = await api_client.api_request("POST", endpoint, payload)
    
    if "logicalId" in response:
        return (response['logicalId'])
    else:
        raise ValueError(f"Failed to fetch logical ID: {response}")

async def get_primary_gateway(api_client, enterprise_id, edge_id):
    """
    Get full edge config and parse logical id of the primary gateway
    """

    primary_gw = {}

    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "edge/getEdgeConfigurationStack",
        "params": {
            "enterpriseId": int(enterprise_id),
            "edgeId": edge_id,
            "with": [
                "modules"
            ]
        }
    }

    endpoint = "/portal/"

    response = await api_client.api_request(
        method="POST",
        endpoint=endpoint,
        payload=payload
    )
    
    for result in response.get("result", []):
        for module in result.get("modules", []):
            gateway_detail = module.get("data", {}).get("gatewaySelection", {}).get("primaryDetail", {})
            if gateway_detail.get("gatewayType") == "PRIMARY":
                primary_gw = {
                    "logicalId": gateway_detail.get("logicalId"),
                    "ipAddress": gateway_detail.get("ipAddress"),
                    "name": gateway_detail.get("name"),
                    "id": gateway_detail.get("id"),
                    "ipV6Address": gateway_detail.get("ipV6Address"),
                    "gatewayType": gateway_detail.get("gatewayType")
                }
    
    return primary_gw


async def get_gw_route_table(api_client, ent_logical_id, gw_logical_id):
    """
    Get Edge routing table websocket
    """

    response = await api_client.websocket_request(
        action="getGwRouteTable",
        data={ 
            "segmentId": 0,
            "logicalId": gw_logical_id,
            "enterpriseLogicalId": ent_logical_id,
        }
    )
    
    routes=response.get("data", {}).get("result", [])
    return routes
    

async def main():
   
    base_url = os.getenv("ORCHESTRATOR_URL")
    token = os.getenv("API_TOKEN")
    enterprise_id = os.getenv("ENTERPRISE_ID")

    edge_id=11
    edge_name="branch2-vedge"

    if not base_url or not token:
        raise ValueError("Missing required environment variables (ORCHESTRATOR_URL, API_TOKEN).")

    api_client = VeloCloudAPI(base_url, token)

    print(f"\n- Getting enterprise logical Id")
    ent_logical_id=await get_enterprise_logical_id(api_client, enterprise_id)
    print(ent_logical_id)

    print(f"\n- Getting primary gateway")
    primary_gw = await get_primary_gateway(api_client, enterprise_id, edge_id)
    print(json.dumps(primary_gw, indent=4))
    
    print("\n- Getting edge route table...")
    routes = await get_gw_route_table(api_client, ent_logical_id, primary_gw['logicalId'])
    print(json.dumps(routes, indent=4))
    
    tunnels_up = any(route.get("peerName") == edge_name and route.get("reachable") for route in routes)
    print(f"\n*** Tunnels to '{edge_name}' are {'UP' if tunnels_up else 'DOWN'} ***")

if __name__ == "__main__":
    asyncio.run(main())
