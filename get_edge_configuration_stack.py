"""

Velocloud Orchestrator API - v1

edge/getEdgeConfigurationStack, "params":{"edgeId":1,"enterpriseId":1,"with":["modules"]}}

Get full edge configuration,using entepriseID and EdgeID.
Parse individual sections of the config by and their path

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



async def get_edge_config(api_client, enterprise_id, edge_id):
    """
    Get Full Edge Configuration
    """

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

    return response
    
def parse_config(json_obj, target_value, config_path=""):
    """
    Recursively searches dict/list to find an object
    with a `name` key matching the `target_value`. 
    Tracks and returns the config path (human-readable).
    """
    if isinstance(json_obj, list):
        for index, item in enumerate(json_obj):
            new_path = f"{config_path}[{index}]"
            result, result_path = parse_config(item, target_value, new_path)
            if result:
                return result, result_path
    elif isinstance(json_obj, dict):
        # Check if the current object matches the target
        if json_obj.get("name") == target_value:
            return json_obj, config_path
        # Update config path with `name` if it exists at this level
        current_path = f"{config_path} > {json_obj.get('name')}" if json_obj.get("name") else config_path
        for key, value in json_obj.items():
            result, result_path = parse_config(value, target_value, current_path)
            if result:
                return result, result_path
    return None, None   

async def main():
   
    base_url = os.getenv("ORCHESTRATOR_URL")
    token = os.getenv("API_TOKEN")
    enterprise_id = os.getenv("ENTERPRISE_ID")

    if not base_url or not token:
        raise ValueError("Missing required environment variables (ORCHESTRATOR_URL, API_TOKEN).")

    api_client = VeloCloudAPI(base_url, token)
    
    edge_id = 1
    response = await get_edge_config(api_client, enterprise_id, edge_id)

    
    """
    Find configuration settings using modules or object names
    modules: analyticsSettings, atpMetadata, deviceSettings, firewall, QOS, WAN
    objects: GE3, "71.0.0.1"

    """
    find_what ="WAN"

    config_object, obj_path = parse_config(response, find_what)
    
    if config_object:
        print(f"Object {find_what} section:")
        print(json.dumps(config_object, indent=4))
        print("\nPath to Object:")
        print(obj_path)

    #print(json.dumps(response, indent=4))

if __name__ == "__main__":
    asyncio.run(main())
