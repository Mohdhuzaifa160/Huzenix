import dateparser

from core.utilities import speak

def parse_natural_date(text):
    parsed_date = dateparser.parse(text)
    if parsed_date is None:
        speak("Sorry, I couldn't understand the date and time.")
        return None
    return parsed_date
