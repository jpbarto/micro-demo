from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import httpx
import asyncio
import socket

app = FastAPI()
app.add_event_handler("startup", lambda: print("Starting up..."))
app.add_event_handler("shutdown", lambda: print("Shutting down..."))

# Replace these URLs with the actual endpoints of the other services
SERVICE_URL_1 = "https://httpbin.org/json"
SERVICE_URL_2 = "https://httpbin.org/json"

async def fetch_service(url: str, number: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params={"number": number})
        response.raise_for_status()
        return response.json()

@app.get("/aggregate")
async def aggregate(number: int = Query(..., description="Number to process")):
    try:
        results = await asyncio.gather(
            fetch_service(SERVICE_URL_1, number),
            fetch_service(SERVICE_URL_2, number)
        )
        combined = {
            # "hostname": socket.gethostname(),
            "service1": results[0],
            "service2": results[1]
        }
        return JSONResponse(content=combined)
    except httpx.HTTPError as e:
        return JSONResponse(status_code=502, content={"error": str(e)})
