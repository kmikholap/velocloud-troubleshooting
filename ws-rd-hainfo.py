"""

Velocloud Remote Diagnostics Websocket API - HA Info
"test": "HA_INFO"

Show High Availability HA details 
This API call as well as a few others do not support JSON formatted response. HTML response must be formatted to remove HTML tags.

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
from bs4 import BeautifulSoup

load_dotenv()

async def get_ha_info(api_client, edge_logical_id):
    """
    Show HA Information
    """
    print(f"Dumping HA information for  {edge_logical_id}...")
    response = await api_client.websocket_request(
        action="runDiagnostics",
        data={
            "logicalId": edge_logical_id,
            "test": "HA_INFO",
        }
    )
    print (response)
    return response


async def main():
    base_url = os.getenv("ORCHESTRATOR_URL")
    token = os.getenv("API_TOKEN")
    enterprise_id = os.getenv("ENTERPRISE_ID")

    if not base_url or not token:
        raise ValueError("Missing required environment variables (ORCHESTRATOR_URL, API_TOKEN).")

    api_client = VeloCloudAPI(base_url, token)
    

    edge_logical_id="986890ec-8fee-4075-9bec-62ee11b0f33e" # Get from enterprise/getEnterpriseEdges (example: get-enterprise-edges.py)

    response =  await get_ha_info(api_client, edge_logical_id)

    # Note!!!! This API call as well as a few others do not support JSON formatted response. Code below prases HTML in to a JSON formatted output using Beautiful soup module 

    html_output = response["data"]["results"]["output"]

    # Parse the HTML
    soup = BeautifulSoup(html_output, "html.parser")

    # Function to extract table data
    def parse_table(header_row, data_rows):
        headers = [header.text.strip() for header in header_row.find_all("span")]
        results = []
        for row in data_rows:
            cells = row.find_all("span")
            results.append({headers[i]: cells[i].text.strip() for i in range(len(headers))})
        return results

    parsed_data = {}

    for section in soup.find_all("h3"):
        section_name = section.text.strip()
        table = section.find_next("div", class_="vce-result-tbl")
        if table:
            header_row = table.find("div", class_="vce-result-header-row")
            data_rows = table.find_all("div", class_="vce-result-data-row")
            parsed_data[section_name] = parse_table(header_row, data_rows)

    # Replace the original HTML in the response with the parsed data
    response["data"]["results"]["output"] = parsed_data

    # Print the JSON structure
    print(json.dumps(response, indent=4))

if __name__ == "__main__":
    asyncio.run(main())
