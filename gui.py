import tkinter as tk
from tkinter import scrolledtext
from core.chatbot import generate_reply
import pyttsx3

# Set up the Text-to-Speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

class MentalHealthApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 Mental Health Companion")
        
        self.chat_history = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=50, height=15, font=("Arial", 12), state=tk.DISABLED)
        self.chat_history.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.user_input = tk.Entry(self.root, width=40, font=("Arial", 12))
        self.user_input.grid(row=1, column=0, padx=10, pady=10)

        self.send_button = tk.Button(self.root, text="Send", width=10, font=("Arial", 12), command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

        self.mood_label = tk.Label(self.root, text="Mood: Neutral", font=("Arial", 12), fg="black")
        self.mood_label.grid(row=2, column=0, columnspan=2, pady=10)

    def send_message(self):
        user_text = self.user_input.get().strip()
        
        if user_text.lower() in ['exit', 'quit', 'bye']:
            self.chat_history.config(state=tk.NORMAL)
            self.chat_history.insert(tk.END, "Bot: Take care of yourself. Talk soon! 💙\n")
            self.chat_history.config(state=tk.DISABLED)
            speak("Take care of yourself. Talk soon!")
            return
        
        self.chat_history.config(state=tk.NORMAL)
        self.chat_history.insert(tk.END, f"You: {user_text}\n")
        
        response = generate_reply(user_text)
        
        # Update mood based on sentiment
        mood = "Neutral"  # This should be dynamically updated based on sentiment analysis
        if "positive" in response.lower():
            mood = "Positive"
            self.mood_label.config(fg="green", text="Mood: Positive")
        elif "negative" in response.lower():
            mood = "Negative"
            self.mood_label.config(fg="red", text="Mood: Negative")
        else:
            self.mood_label.config(fg="black", text="Mood: Neutral")
        
        self.chat_history.insert(tk.END, f"Bot: {response}\n")
        self.chat_history.config(state=tk.DISABLED)
        self.user_input.delete(0, tk.END)
        
        # Read bot response aloud
        speak(response)

# Set up the Tkinter window
root = tk.Tk()
app = MentalHealthApp(root)
root.mainloop()
