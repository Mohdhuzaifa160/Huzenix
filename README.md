<h1 align="center">🤖 Huzenix – Python Voice Assistant for Termux</h1>

<p align="center">
  <img src="https://img.shields.io/github/languages/top/MohdHuzaifa160/Huzenix?color=yellow&style=for-the-badge" />
  <img src="https://img.shields.io/github/last-commit/MohdHuzaifa160/Huzenix?style=for-the-badge" />
  <img src="https://img.shields.io/github/repo-size/MohdHuzaifa160/Huzenix?color=blue&style=for-the-badge" />
</p>

<p align="center">
  <b>Huzenix</b> is a smart AI voice assistant built using Python and Termux.  
  It works both <b>online and offline</b>, and supports commands like reminders, calculator, notes, file manager, weather, news, and more!
</p>

---

## 🌟 Features

- 🎙️ Voice commands (online + offline)
- 🧮 Calculator with voice input
- 🗒️ Notes creator and reader
- ⏰ Smart reminders (natural language support)
- 🌦️ Weather info using API
- 📰 News updates
- 📁 File manager (voice-driven)
- 🧠 AI Conversation Mode
- 🛑 Sleep, Debug, and Error Modes
- 🔒 Works inside **Termux** on Android!

---

## 🚀 Tech Stack

| Language | Tools/Libraries     |
|----------|---------------------|
| Python   | `speech_recognition`, `pyttsx3`, `datetime`, `schedule`, `requests`, `termux-api`, `os`, `re`, `json` |
| Platform | Termux + Android    |

---

## 🛠️ Installation (Termux)

```bash
pkg update && pkg upgrade
pkg install python
pkg install termux-api
pip install -r requirements.txt
