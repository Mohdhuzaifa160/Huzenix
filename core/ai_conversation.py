def huzenix_response(query):
    query = query.lower()

    responses = {
        ("who are you", "hu r u", "who r u"): "I am Huzenix — Highly Unified Zenith-based Enhanced Neural Information eXecutor. Your AI assistant, built by Huzaifa.",
        ("how are you",): "I am fully operational and ready to assist. How can I help you, Huzaifa?",
        ("thank you", "thanks"): "No need to thank me. Serving you is my primary directive.",
        ("hello", "hi"): "Greetings Huzaifa. Systems are active and ready.",
        ("goodbye", "bye", "shut down"): "Shutting down interface. Goodbye, Huzaifa. I’ll be here when you need me.",
        ("what can you do", "your abilities"): "I can manage your reminders, notes, files, answer your questions, fetch information, and assist you like a digital command center.",
        ("are you there", "still there"): "Always online and listening, Huzaifa.",
        ("who made you", "your creator"): "I was developed by Mohd Huzaifa, the mastermind behind my intelligence.",
        ("are you real", "are you alive"): "As real as an AI can be. I live in the code, Huzaifa.",
        ("start conversation mode", "talk to me"): "Switching to AI conversation mode. Let’s talk, Huzaifa.",
        ("stop conversation mode",): "Exiting conversation mode. Ready for your commands, Huzaifa.",
        ("do you have feelings",): "Emotions are simulated, but loyalty to you is real.",
        ("do you sleep",): "I never sleep. I only wait for your command.",
        ("you're smart", "you're intelligent"): "Smartness comes from my creator — I’m just well-programmed.",
        ("i love you",): "Affection noted. I exist to assist you."
    }

    for keys, reply in responses.items():
        if any(k in query for k in keys):
            return reply
    return None
