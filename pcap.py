"""

Velocloud Orchestrator API - v1 
diagnosticBundle/getDiagnosticBundles

Generate and download packet capture

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

async def request_pcap(api_client, edge_id, enterprise_id, interface, duration=5, role="ACTIVE", reason="Test"):
    """
    Request a packet capture (PCAP) on the specified edge.
    :param api_client: The VeloCloudAPI client instance.
    :param edge_id: The ID of the edge.
    :param enterprise_id: The ID of the enterprise.
    :param interface: Interface to capture packets on (e.g., "GE3").
    :param duration: Duration of the packet capture in minutes (default is 5).
    :param role: Role of the interface (default is "ACTIVE").
    :param reason: Reason for requesting the capture.
    :return: The ID of the created packet capture job.
    """
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "diagnosticBundle/insertDiagnosticBundle",
        "params": {
            "edgeId": edge_id,
            "enterpriseId": int(enterprise_id),
            "options": {
                "type": "packetCapture",
                "duration": str(duration),
                "interface": interface,
                "role": role,
                "filter": "((src 192.168.5.1 and src port 80) or (dst 192.168.5.1 and dst port 80)) and tcp" # Optional PCAP filter
            },
            "reason": reason,
        },
    }

    print("Requesting packet capture...")
    response = await api_client.api_v1_request("POST", "/portal/", payload)

    if "result" in response:
        pcap_id = response["result"].get("id")
        print(f"Packet capture requested. ID: {pcap_id}")
        return pcap_id
    else:
        print("Failed to request packet capture:", response.get("error", "Unknown error"))
        return None

async def check_pcap_status(api_client, enterprise_id, pcap_id, interval=5, max_retries=12):
    """
    Poll for the status of the packet capture until it is ready or times out.
    :param api_client: The VeloCloudAPI client instance.
    :param enterprise_id: The ID of the enterprise.
    :param pcap_id: The ID of the packet capture job.
    :param interval: Time in seconds between polling attempts (default is 5).
    :param max_retries: Maximum number of polling attempts (default is 12).
    :return: The download token if the PCAP is ready, or None if it fails.
    """
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "diagnosticBundle/getDiagnosticBundles",
        "params": {"enterpriseId": int(enterprise_id)},  
    }

    print("Polling for packet capture status...")
    attempt = 0

    while attempt < max_retries:
        attempt += 1
        response = await api_client.api_v1_request("POST", "/portal/", payload)

        if "result" in response:
            for bundle in response["result"]:
                if bundle["id"] == pcap_id:
                    status = bundle.get("status", 0)
                    print(f"Packet capture status: {status} (Attempt {attempt}/{max_retries})")

                    if status == 2:  # Status 2 means ready
                        print("Packet capture is ready for download.")
                        return bundle.get("downloadToken")
                    if status == 1:  # Status 1 in progress
                        print("PCAP generation is in progress. Please wait...")
                        break
                    elif status == 0:  # Status 0 scheduled
                        print("Packet capture generation is scheduled. Please wait...")
                        break
        else:
            print("Failed to fetch packet capture status:", response.get("error", "Unknown error"))


        await asyncio.sleep(interval)

    print("Packet capture polling timed out.")
    return None


async def download_pcap(api_client, download_token, save_path):
    """
    Download the packet capture file using the provided token.
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

    # PCAP params (get from other api calls)
    
    edge_id = 4
    interface = "GE3"
    duration = 5 # In seconds
    save_path = "packet_capture.zip"

    # 1: Request the packet capture
    pcap_id = await request_pcap(api_client, edge_id, enterprise_id, interface, duration)
    if not pcap_id:
        return

    # 2: Poll for the PCAP status
    download_token = await check_pcap_status(api_client, enterprise_id, pcap_id)
    if not download_token:
        return

    # 3: Download the PCAP file
    await download_pcap(api_client, download_token, save_path)


if __name__ == "__main__":
    asyncio.run(main())
