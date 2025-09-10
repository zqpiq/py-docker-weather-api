from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()


def get_weather() -> dict[str, Any]:
    url = "https://wttr.in/Paris?format=j1"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    current = data["current_condition"][0]
    temp_c = current["temp_C"]
    speed_wind = current["windspeedKmph"]
    visibility = current["visibility"]
    return {
        "city": "Paris",
        "celsius": temp_c,
        "wind speed": speed_wind,
        "visibility": visibility
    }


if __name__ == "__main__":
    get_weather()
