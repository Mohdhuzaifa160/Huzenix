import json
import schedule
from datetime import datetime
from zoneinfo import ZoneInfo
import dateparser

from core.voice_output import speak
from core.voice_input import listen

MEMORY_FILE = "memory.json"
reminders = []

def load_memory():
    try:
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_memory(data):
    with open(MEMORY_FILE, "w") as file:
        json.dump(data, file, indent=4)

memory = load_memory()
reminders = memory.get("reminders", [])

def set_reminder(reminder_text, reminder_time_str, city=None, tag="uncategorized"):
    timezone_str = "Asia/Kolkata"
    settings = {'TIMEZONE': timezone_str, 'RETURN_AS_TIMEZONE_AWARE': True}
    reminder_time = dateparser.parse(reminder_time_str, settings=settings)

    if reminder_time is None:
        speak("Sorry, I couldn't understand the reminder time.")
        return False

    reminder_utc = reminder_time.astimezone(ZoneInfo("UTC"))

    reminders.append({
        "text": reminder_text,
        "time": reminder_utc.strftime("%Y-%m-%d %H:%M:%S"),
        "city": city if city else "default (IST)",
        "tag": tag
    })

    save_memory({"reminders": reminders})
    speak(f"Reminder set for {reminder_time.strftime('%A, %d %B %Y at %I:%M %p')} under category '{tag}'")
    return True

def show_reminders():
    now_utc = datetime.now(ZoneInfo("UTC"))

    if not reminders:
        speak("You have no reminders saved.")
        return

    speak("Do you want to see all reminders, only upcoming, expired, or reminders by tag?")
    choice = listen().lower()

    filtered = []
    if "upcoming" in choice:
        filtered = [r for r in reminders if datetime.strptime(r["time"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=ZoneInfo("UTC")) > now_utc]
    elif "old" in choice or "expired" in choice:
        filtered = [r for r in reminders if datetime.strptime(r["time"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=ZoneInfo("UTC")) <= now_utc]
    elif "tag" in choice:
        speak("Please say the tag you want to filter by.")
        tag = listen().lower()
        filtered = [r for r in reminders if r.get("tag", "uncategorized") == tag]
    else:
        filtered = reminders

    if not filtered:
        speak("No reminders found for the selected option.")
    else:
        speak(f"You have {len(filtered)} reminders:")
        for r in filtered:
            reminder_time = datetime.strptime(r["time"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=ZoneInfo("UTC")).astimezone(ZoneInfo("Asia/Kolkata"))
            speak(f"{r['text']} at {reminder_time.strftime('%d %B %Y, %I:%M %p')} in {r['city']} under {r['tag']} tag")

def check_reminders():
    now_utc = datetime.now(ZoneInfo("UTC"))
    to_remove = []

    for i, reminder in enumerate(reminders):
        reminder_time = datetime.strptime(reminder["time"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=ZoneInfo("UTC"))
        if now_utc >= reminder_time:
            speak(f"Reminder: {reminder['text']} (set for {reminder['time']} UTC)")
            to_remove.append(i)

    for i in reversed(to_remove):
        reminders.pop(i)

    save_memory({"reminders": reminders})
