from datetime import datetime
from core.voice_output import speak
from core.voice_input import listen

def save_note():
    speak("What should I write?")
    note = listen()
    if note:
        with open("huzenix_notes.txt", "a") as f:
            f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M')} - {note}\n")
        speak("Note saved successfully.")

def read_notes():
    try:
        with open("huzenix_notes.txt", "r") as f:
            notes = f.readlines()
            if notes:
                speak("Here are your notes.")
                for n in notes:
                    print(n.strip())
                    speak(n.strip())
            else:
                speak("You don't have any notes.")
    except FileNotFoundError:
        speak("You don't have any notes yet.")

def delete_notes():
    try:
        open("huzenix_notes.txt", "w").close()
        speak("All your notes have been deleted.")
    except Exception as e:
        speak("Sorry, I was unable to delete the notes.")
        print(f"Error deleting notes: {e}")
