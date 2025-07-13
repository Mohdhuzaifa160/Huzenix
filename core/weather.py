import requests
from core.voice_output import speak

def get_weather(query, memory):
    last_city = memory.get("last_city", "Lucknow")  # Default fallback

    try:
        words = query.lower().split()
        if "in" in words:
            city_index = words.index("in") + 1
            city = " ".join(words[city_index:])
            memory["last_city"] = city
        else:
            city = last_city

        api_key = "fcf22f756e444ff581755a4bf25fc48e"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            return f"Weather info for '{city}' not found."

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"].capitalize()
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]

        return f"The weather in {city} is {desc} with {temp}°C (feels like {feels_like}°C), humidity {humidity}%."
    except Exception as e:
        return "Error fetching weather info."
