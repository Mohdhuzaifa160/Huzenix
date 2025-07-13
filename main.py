import schedule
import webbrowser
from datetime import datetime

from core.voice_input import listen
from core.voice_output import speak
from core.weather import get_weather
from core.news import get_news
from core.file_manager import file_management
from core.notes import take_note, read_notes, delete_notes
from core.reminder import set_reminder, show_reminders, check_reminders
from core.chatbot import get_openai_answer, get_wolfram_answer, offline_calculator
from core.calculator import simple_calculator
from core.timezone_helper import get_time_in_timezone
from core.ai_conversation import huzenix_response
from core.date_parser import parse_natural_date
from core.voice_input import wait_for_wake_word

def main():
    wait_for_wake_word()
    schedule.every(1).minutes.do(check_reminders)

    while True:
        schedule.run_pending()
        query = listen()
        if not query:
            continue
        query = query.lower()

        # Core voice actions
        if "show reminders" in query or "view reminders" in query:
            show_reminders()

        elif "time in" in query:
            city = query.split("time in")[-1].strip()
            city_time = get_time_in_timezone(city)
            if city_time:
                speak(f"The time in {city.title()} is {city_time}")
            else:
                speak(f"Sorry, I don't have timezone information for {city}.")

        elif "time" in query:
            speak(f"The time is {datetime.now().strftime('%I:%M %p')}")

        elif "date" in query:
            speak(f"Today's date is {datetime.now().strftime('%A, %d %B %Y')}")

        elif "weather" in query:
            speak(get_weather(query))

        elif "news" in query:
            speak(get_news())

        elif "open youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif "make a note" in query or "take a note" in query:
            take_note()

        elif "read my notes" in query or "show my notes" in query:
            read_notes()

        elif "delete my notes" in query or "clear my notes" in query:
            delete_notes()

        elif "set reminder" in query or "add reminder" in query:
            speak("What should I remind you?")
            reminder_msg = listen().lower()

            speak("When should I remind you?")
            reminder_time_str = listen().lower()

            # Handle vague time
            vague_time_defaults = {
                "morning": "5 am", "afternoon": "1 pm", "evening": "6 pm", "night": "9 pm"
            }

            for vague_term, suggested_time in vague_time_defaults.items():
                if vague_term in reminder_time_str:
                    speak(f"Did you mean {suggested_time}? Say yes to confirm or no to correct it.")
                    user_response = listen().lower()
                    if "yes" in user_response:
                        reminder_time_str = reminder_time_str.replace(vague_term, suggested_time)
                    else:
                        speak("Please tell me the correct time.")
                        corrected_time = listen().lower()
                        reminder_time_str = reminder_time_str.replace(vague_term, corrected_time)
                    break

            speak("Do you want to add a category or tag for this reminder?")
            tag_response = listen().lower()
            reminder_tag = "uncategorized"
            if "yes" in tag_response:
                speak("Please say the category or tag.")
                reminder_tag = listen().lower()

            date_time_obj = parse_natural_date(reminder_time_str)

            if date_time_obj:
                set_reminder(reminder_msg, reminder_time_str, tag=reminder_tag)
            else:
                speak("Sorry, I couldn't understand the date and time.")

        elif "file" in query:
            file_management(query)

        elif "calculate" in query or "what is" in query:
            answer = offline_calculator(query)
            speak(answer)

        elif "exit" in query or "stop" in query:
            speak("Goodbye!")
            break

        else:
            # Smart chatbot fallback
            response = huzenix_response(query)
            if response:
                speak(response)
            else:
                answer = get_wolfram_answer(query)
                if "WolframAlpha error" in answer:
                    answer = offline_calculator(query)
                if "couldn't" in answer:
                    answer = get_openai_answer(query)
                speak(answer)

if __name__ == "__main__":
    main()
