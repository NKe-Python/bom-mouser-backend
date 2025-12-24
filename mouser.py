import os
import requests

API_KEY = os.getenv("MOUSER_API_KEY")
BASE_URL = "https://api.mouser.com/api/v1/search/partnumber"

def search_mouser(mpn: str):
    payload = {
        "SearchByPartRequest": {
            "mouserPartNumber": mpn,
            "partSearchOptions": "Exact"
        }
    }

    response = requests.post(
        BASE_URL,
        params={"apiKey": API_KEY},
        headers={"Content-Type": "application/json"},
        json=payload,
        timeout=10
    )

    response.raise_for_status()
    return response.json()