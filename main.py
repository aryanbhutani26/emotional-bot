from core.chatbot import generate_reply
import speech_recognition as sr
import pyttsx3
import os


# Initialize text-to-speech engine
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Voice input function
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Speak now...")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that."
        except sr.RequestError:
            return "Voice service error."

# Load or set AI name
def get_ai_name():
    filename = "ai_name.txt"
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return f.read().strip()
    else:
        name = input("💬 What do you want to name your AI Companion?\nName: ").strip().title()
        with open(filename, "w") as f:
            f.write(name)
        return name

# --- Main ---
ai_name = get_ai_name()
print(f"\n🧠 {ai_name} - Mental Health Companion")
print("Type 'exit' or 'quit' to stop.\n")

exit_commands = ['exit', 'quit', 'bye', 'exiy']

while True:
    mode = input("Choose input mode (text / voice): ").strip().lower()

    if mode == "voice":
        user_input = listen()
        print(f"You (voice): {user_input}")
    else:
        user_input = input("You: ").strip()

    if user_input.lower() in exit_commands:
        farewell = "Take care of yourself. Talk soon! 💙"
        print(f"{ai_name}: {farewell}")
        speak(farewell)
        break

    response = generate_reply(user_input)
    print(f"{ai_name}:", response)
    speak(response)
