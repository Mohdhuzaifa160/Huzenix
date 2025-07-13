import os

def speak(text):
    print("Speaking:", text)
    os.system(f'termux-tts-speak "{text}"')
