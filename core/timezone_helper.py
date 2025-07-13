from datetime import datetime
import pytz

timezones_map = {
    "new york": "America/New_York",
    "tokyo": "Asia/Tokyo",
    "london": "Europe/London",
    "delhi": "Asia/Kolkata",
    "mumbai": "Asia/Kolkata",
    "bangalore": "Asia/Kolkata",
    "paris": "Europe/Paris",
    "berlin": "Europe/Berlin",
    "sydney": "Australia/Sydney",
    "melbourne": "Australia/Melbourne",
    "dubai": "Asia/Dubai",
    "moscow": "Europe/Moscow",
    "beijing": "Asia/Shanghai",
    "shanghai": "Asia/Shanghai",
    "los angeles": "America/Los_Angeles",
    "san francisco": "America/Los_Angeles",
    "chicago": "America/Chicago",
    "toronto": "America/Toronto",
    "vancouver": "America/Vancouver",
    "singapore": "Asia/Singapore",
    "seoul": "Asia/Seoul",
    "hong kong": "Asia/Hong_Kong"
}

def get_time_in_timezone(city_name):
    city_name = city_name.lower()
    if city_name not in timezones_map:
        return None
    tz_name = timezones_map[city_name]
    timezone = pytz.timezone(tz_name)
    city_time = datetime.now(timezone)
    return city_time.strftime("%Y-%m-%d %H:%M:%S")
