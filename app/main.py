import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()


def get_weather() -> dict[str, Any]:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY does not exist")
    city = "Paris"
    url = "http://api.weatherapi.com/v1/current.json"
    params = {"key": api_key, "q": city}
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    return data


if __name__ == "__main__":
    get_weather()
