#!/usr/bin/env python

import json
import os

import requests


# Weather icons mapping for wttr.in weather codes
WEATHER_CODES = {
    "113": "☀️",
    "116": "⛅️",
    "119": "☁️",
    "122": "☁️",
    "143": "🌫",
    "176": "🌦",
    "179": "🌧",
    "182": "🌧",
    "185": "🌧",
    "200": "⛈",
    "227": "🌨",
    "230": "❄️",
    "248": "🌫",
    "260": "🌫",
    "263": "🌦",
    "266": "🌦",
    "281": "🌧",
    "284": "🌧",
    "293": "🌦",
    "296": "🌦",
    "299": "🌧",
    "302": "🌧",
    "305": "🌧",
    "308": "🌧",
    "311": "🌧",
    "314": "🌧",
    "317": "🌧",
    "320": "🌨",
    "323": "🌨",
    "326": "🌨",
    "329": "❄️",
    "332": "❄️",
    "335": "❄️",
    "338": "❄️",
    "350": "🌧",
    "353": "🌦",
    "356": "🌧",
    "359": "🌧",
    "362": "🌧",
    "365": "🌧",
    "368": "🌨",
    "371": "❄️",
    "374": "🌧",
    "377": "🌧",
    "386": "⛈",
    "389": "🌩",
    "392": "⛈",
    "395": "❄️",
}


# Set WEATHER_LOCATION in the environment to change the location.
LOCATION = os.getenv("WEATHER_LOCATION", "Lagos")

data = {}

try:
    weather = requests.get(
        f"https://wttr.in/{LOCATION}?format=j1",
        timeout=10,
    ).json()

    current = weather["current_condition"][0]

    temp = current["temp_C"]
    code = current["weatherCode"]

    data["text"] = f"{WEATHER_CODES.get(code, '✨')} {temp}°C"

    tooltip = f"<b>{LOCATION}</b>\n"
    tooltip += f"Condition: {current['weatherDesc'][0]['value']}\n"
    tooltip += f"Feels like: {current['FeelsLikeC']}°C\n"
    tooltip += f"Humidity: {current['humidity']}%\n"
    tooltip += f"Wind: {current['windspeedKmph']} Km/h\n\n"

    for day in weather["weather"][:3]:
        tooltip += (
            f"<b>{day['date']}</b>: "
            f"⬆️{day['maxtempC']}° "
            f"⬇️{day['mintempC']}°\n"
        )

    data["tooltip"] = tooltip

except (requests.RequestException, KeyError, IndexError, ValueError):
    data["text"] = "󰖪 Weather Error"

print(json.dumps(data))
