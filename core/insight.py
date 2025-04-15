import csv
from collections import Counter
from datetime import datetime, timedelta

log_file = 'mood_log.csv'

def generate_weekly_summary():
    try:
        moods = []

        with open(log_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            # Only consider entries from the last 7 days
            for row in reader:
                timestamp = datetime.strptime(row["Timestamp"], "%Y-%m-%d %H:%M:%S")
                if datetime.now() - timestamp <= timedelta(days=7):
                    moods.append(row["Mood"])

        if not moods:
            return "Hmm, I don’t have enough data to summarize your week yet. Try chatting with me more!"

        # Count each mood
        mood_counts = Counter(moods)
        top_mood = mood_counts.most_common(1)[0][0]

        emoji_map = {
            "positive": "😊",
            "neutral": "😐",
            "negative": "😔"
        }

        summary = f"""
🗓️ **Your Weekly Mood Summary**
———————————————
Total entries: {len(moods)}
Most frequent mood: {top_mood.capitalize()} {emoji_map.get(top_mood, '')}

Mood breakdown:
Positive: {mood_counts.get("positive", 0)} 😊
Neutral: {mood_counts.get("neutral", 0)} 😐
Negative: {mood_counts.get("negative", 0)} 😔

Keep checking in! I'm always here for you. 💙
        """.strip()

        return summary

    except FileNotFoundError:
        return "No mood data found yet. Let's start chatting!"
        
def suggest_based_on_mood():
    try:
        moods = []
        with open(log_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                moods.append(row["Mood"])

        if not moods:
            return "I don’t have enough data yet for suggestions."

        mood_counts = Counter(moods)
        total = sum(mood_counts.values())

        suggestions = []

        if mood_counts["negative"] > total * 0.4:
            suggestions.append("You've had a lot of heavy days lately. Try a digital detox or write a private journal entry.")
        if mood_counts["positive"] > total * 0.5:
            suggestions.append("You're doing really well lately! Keep doing what works for you. 💪")
        if mood_counts["neutral"] > total * 0.5:
            suggestions.append("You're feeling neutral often. Maybe explore something new to boost your mood.")

        return "\n".join(suggestions) if suggestions else "Keep checking in. You're doing your best! 💙"

    except:
        return "Couldn’t generate suggestions yet. Let’s try again later!"

