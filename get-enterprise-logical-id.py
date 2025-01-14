"""
Velocloud Orchestrator API - v1
/enterprise/getEnterprise

Get enterprise logicalId 

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

async def get_enterprise_logical_id(api_client, enterprise_id):
    """
    Fetch the logical ID of an enterprise using API v1.
    """
    endpoint = "/portal/rest/enterprise/getEnterprise"
    payload = {
        "id": int(enterprise_id)
    } 
    response = await api_client.api_request("POST", endpoint, payload)
    print (response)
    if "logicalId" in response:
        return response["id","logicalId",""]
    else:
        raise ValueError(f"Failed to fetch logical ID: {response}")


async def main():
    base_url = os.getenv("ORCHESTRATOR_URL")
    token = os.getenv("API_TOKEN")
    enterprise_id = os.getenv("ENTERPRISE_ID")

    if not base_url or not token:
        raise ValueError("Missing required environment variables (ORCHESTRATOR_URL, API_TOKEN).")

    api_client = VeloCloudAPI(base_url, token)

    response =  await get_enterprise_logical_id(api_client,enterprise_id)

    if "error" in response:
        print(f"Encountered the following error: {response['error']}")
    else:
        print("Results:")
        print(json.dumps(response, indent=4))

if __name__ == "__main__":
    asyncio.run(main())

