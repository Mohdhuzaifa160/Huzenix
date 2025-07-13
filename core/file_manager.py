import os
from core.voice_output import speak

def file_management(command):
    try:
        if "create file" in command:
            filename = command.replace("create file", "").strip()
            with open(filename, "w") as f:
                f.write("")
            speak(f"File {filename} created.")

        elif "delete file" in command:
            filename = command.replace("delete file", "").strip()
            if os.path.exists(filename):
                os.remove(filename)
                speak(f"File {filename} deleted.")
            else:
                speak("File not found.")

        elif "list files" in command:
            files = os.listdir()
            speak("Files in the directory are: " + ", ".join(files))

        elif "read file" in command:
            filename = command.replace("read file", "").strip()
            if os.path.exists(filename):
                with open(filename, "r") as f:
                    content = f.read()
                speak(f"Content of {filename} is: {content}")
            else:
                speak("File not found.")

        elif "rename file" in command:
            parts = command.replace("rename file", "").strip().split(" to ")
            if len(parts) == 2:
                old_name, new_name = parts
                if os.path.exists(old_name.strip()):
                    os.rename(old_name.strip(), new_name.strip())
                    speak(f"File renamed from {old_name} to {new_name}")
                else:
                    speak("Original file not found.")
            else:
                speak("Please specify both old and new file names.")

    except Exception as e:
        speak("An error occurred while managing the file.")
