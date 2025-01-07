import aiohttp
import json
import ssl
import websockets


class VeloCloudAPI:
    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.token = token

    def get_headers(self):
        """
        Generate headers using token-based authentication.
        """
        return {"Authorization": f"Token {self.token}", "Content-Type": "application/json"}

    async def api_request(self, method, endpoint, payload=None):
        """
        Handle Velo API requests.
        """
        url = f"https://{self.base_url}{endpoint}"
        headers = self.get_headers()
        connector = aiohttp.TCPConnector(ssl=False)

        async with aiohttp.ClientSession(headers=headers, connector=connector) as session:
            try:
                if method.upper() == "POST":
                    async with session.post(url, json=payload) as response:
                        return await self.handle_response(response)
                elif method.upper() == "GET":
                    async with session.get(url, params=payload) as response:
                        return await self.handle_response(response)
                else:
                    raise ValueError(f"Unsupported HTTP method: {method}")
            except Exception as e:
                return {"error": str(e)}

    async def websocket_request(self, action, data=None):
        """
        Make a generic WebSocket request.
        :param action: The action to perform (e.g., 'runDiagnostics').
        :param data: The payload data for the WebSocket request.
        :return: WebSocket response.
        """
        diagnostics_url = f"wss://{self.base_url}/ws/"
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE

        headers = [("Authorization", f"Token {self.token}")]
        try:
            async with websockets.connect(diagnostics_url, extra_headers=headers, ssl=ssl_context) as ws:
                # Initial handshake and token retrieval
                token_msg = json.loads(await ws.recv())
                if "token" not in token_msg:
                    return {"error": "WebSocket did not return a valid token."}

                ws_token = token_msg["token"]
                payload = {"action": action, "data": data or {}, "token": ws_token}

                # Send the request
                await ws.send(json.dumps(payload))

                # Receive and return the response
                response = json.loads(await ws.recv())
                return response
        except Exception as e:
            return {"error": str(e)} 
        
    async def download_file(self, endpoint, save_path):
        """
        Download a file from the VeloCloud API.
        :param endpoint: The API endpoint for the file download.
        :param save_path: The local path to save the downloaded file.
        :return: None
        """
        url = f"https://{self.base_url}{endpoint}"
        headers = self.get_headers()

        print("Downloading file")
        connector = aiohttp.TCPConnector(ssl=False)

        async with aiohttp.ClientSession(headers=headers, connector=connector) as session:
            try:
                async with session.get(url) as response:
                    if response.status == 200:
                        with open(save_path, "wb") as f:
                            f.write(await response.read())
                        print(f"File downloaded successfully: {save_path}")
                    else:
                        print(f"Failed to download file. HTTP Status: {response.status}")
            except Exception as e:
                print(f"Error downloading file: {str(e)}")
    
    

    async def handle_response(self, response):
        """
        Handle HTTP responses and decode JSON or log errors.
        """
        try:
            if response.status >= 200 and response.status < 300:
                return await response.json()
            else:
                return {
                    "error": f"HTTP {response.status}: {await response.text()}",
                }
        except aiohttp.ContentTypeError:
            return {"error": f"Unexpected response format: {await response.text()}"}
