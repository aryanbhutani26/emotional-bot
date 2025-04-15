import json
import os
from datetime import datetime

PROFILE_FILE = "user_profile.json"

def load_user_profile():
    if os.path.exists(PROFILE_FILE):
        with open(PROFILE_FILE, "r") as file:
            return json.load(file)
    else:
        return {"name": "", "goals": [], "triggers": [], "mood_history": []}

def save_user_profile(profile):
    with open(PROFILE_FILE, "w") as file:
        json.dump(profile, file, indent=4)

def remember_mood(mood):
    profile = load_user_profile()
    profile["mood_history"].append({"mood": mood, "time": datetime.now().isoformat()})
    save_user_profile(profile)

def set_goal(goal):
    profile = load_user_profile()
    if goal not in profile["goals"]:
        profile["goals"].append(goal)
        save_user_profile(profile)

def add_trigger(trigger):
    profile = load_user_profile()
    if trigger not in profile["triggers"]:
        profile["triggers"].append(trigger)
        save_user_profile(profile)

def get_suggestions():
    profile = load_user_profile()
    suggestions = []

    if profile["goals"]:
        suggestions.append("🌱 Keep working on your goals: " + ", ".join(profile["goals"]))
    if profile["triggers"]:
        suggestions.append("⚠️ Avoid things that trigger you: " + ", ".join(profile["triggers"]))
    
    # Check mood trends
    recent_moods = [entry["mood"] for entry in profile["mood_history"][-5:]]
    if recent_moods.count("Sad") >= 3:
        suggestions.append("💡 You’ve been down lately. Consider talking to a trusted friend or journaling.")
    if recent_moods.count("Happy") >= 3:
        suggestions.append("😊 You've been doing great lately. Keep it up!")

    return suggestions
