"""

Velocloud Orchestrator API - v1 
diagnosticBundle/getDiagnosticBundles

Generate and download diagnostics bundle

Reference: Unpublished API

"""

import asyncio
import os
import json
from dotenv import load_dotenv
from velocloud_api import VeloCloudAPI
import datetime
import time
from urllib.parse import urlencode
import aiohttp


load_dotenv()

async def request_diag_bundle(api_client, edge_id, enterprise_id, reason="Test"):
    """
    Request a diagnostics bundle from the specified edge.
    :param api_client: The VeloCloudAPI client instance.
    :param edge_id: The ID of the edge.
    :param enterprise_id: The ID of the enterprise.
    :param reason: Reason for requesting the diag.
    :return: The ID of the created diag bundle job.
    """
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "diagnosticBundle/insertDiagnosticBundle",
        "params": {
            "edgeId": edge_id,
            "enterpriseId": int(enterprise_id),
            "options": {
                "type": "diagnosticDump"
            },
            "reason": reason,
        },
    }

    print("Requesting diag_bundle...")
    response = await api_client.api_v1_request("POST", "/portal/", payload)

    if "result" in response:
        diag_id = response["result"].get("id")
        print(f"Diag bundle requested. ID: {diag_id}")
        return diag_id
    else:
        print("Failed to request diagnostic bundle:", response.get("error", "Unknown error"))
        return None

async def check_diag_status(api_client, enterprise_id, diag_id, interval=5, max_retries=100):
    """
    Poll for the status of the diag bundle until it is ready or times out.
    :param api_client: The VeloCloudAPI client instance.
    :param enterprise_id: The ID of the enterprise.
    :param diag_id: The ID of the diag job.
    :param interval: Time in seconds between polling attempts (default is 5).
    :param max_retries: Maximum number of polling attempts (default is 100).
    :return: The download token if the diag bundle is ready, or None if it fails.
    """
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "diagnosticBundle/getDiagnosticBundles",
        "params": {"enterpriseId": int(enterprise_id)}, 
    }

    print("Polling for diag bundle status...")
    attempt = 0

    while attempt < max_retries:
        attempt += 1
        response = await api_client.api_v1_request("POST", "/portal/", payload)

        if "result" in response:
            for bundle in response["result"]:
                if bundle["id"] == diag_id:
                    status = bundle.get("status", 0)
                    print(f"Diag bundle status: {status} (Attempt {attempt}/{max_retries})")

                    if status == 2:  # Status 2 means ready
                        print("Diag bundle is ready for download.")
                        return bundle.get("downloadToken")
                    if status == 1:  # Status 1 in progress
                        print("Diag bundle generation is in progress.")
                        break
                    elif status == 0:  # Status 0 scheduled
                        print("Diag bundle generation is scheduled. Please wait.....")
                        break
        else:
            print("Failed to fetch diag bundle status:", response.get("error", "Unknown error"))

        
        await asyncio.sleep(interval)

    print("Diag bundle polling timed out.")
    return None


async def download_diag(api_client, download_token, save_path):
    """
    Download the diag bundle file using the provided token.
    :param api_client: The VeloCloudAPI client instance.
    :param download_token: The token for downloading the PCAP.
    :param save_path: The path to save the downloaded file.
    :return: None
    """
    endpoint = f"/portal/fileDownload?downloadToken={download_token}"
    await api_client.download_file(endpoint, save_path)


async def main():
    base_url = os.getenv("ORCHESTRATOR_URL")
    token = os.getenv("API_TOKEN")
    enterprise_id = os.getenv("ENTERPRISE_ID")

    if not base_url or not token:
        raise ValueError("Missing required environment variables (ORCHESTRATOR_URL, API_TOKEN).")

    api_client = VeloCloudAPI(base_url, token)

    # Diag Bundle params (get from other api calls)
    edge_id = 4
    reason="My test"
    save_path = "diag_bundle.zip"

    diag_id = await request_diag_bundle(api_client, edge_id, enterprise_id, reason)
    if not diag_id:
        return

    download_token = await check_diag_status(api_client, enterprise_id, diag_id)
    if not download_token:
        return

    await download_diag(api_client, download_token, save_path)


if __name__ == "__main__":
    asyncio.run(main())

