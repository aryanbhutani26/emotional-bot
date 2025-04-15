from core.sentiment import detect_sentiment
from core.intent import detect_intent
from core.logger import log_interaction
from core.insight import generate_weekly_summary
from core.goals import save_goal_or_trigger, view_goals_and_triggers
from core.memory import remember_mood, get_suggestions  # 🆕 Emotional memory

def generate_reply(user_input):
    mood = detect_sentiment(user_input)
    intent = detect_intent(user_input)

    # Log the interaction
    log_interaction(user_input, mood, intent)

    # Save mood to emotional memory
    remember_mood(mood)  # 🆕 Stores mood in memory.json

    # Weekly summary
    if "how was my week" in user_input.lower() or "how have i been" in user_input.lower():
        return generate_weekly_summary()

    # AI suggestions based on mood history and user profile
    if "suggest" in user_input.lower() or "advice" in user_input.lower():
        suggestions = get_suggestions()
        if suggestions:
            return "\n".join(suggestions)
        else:
            return "You're doing well! No specific advice right now. 🙂"

    # Save user goals/triggers
    if "goal:" in user_input.lower() or "trigger:" in user_input.lower():
        return save_goal_or_trigger(user_input)

    # View saved goals and triggers
    if "show goals" in user_input.lower() or "show triggers" in user_input.lower():
        return view_goals_and_triggers()

    # Intent-based replies
    if intent == "venting":
        return "I'm really sorry you're feeling that way. You're not alone, and I'm here to listen. 💙"

    if intent == "seeking_help":
        return "It’s okay to ask for help. Try to talk to someone you trust or seek professional support. You matter. 💫"

    if intent == "calming_tip":
        return "Here’s a calming tip: Take 5 deep breaths, close your eyes, and slowly count to 10. 🧘‍♂️"

    if intent == "gratitude":
        return "You're very welcome. I'm always here when you need someone. 🌟"

    if intent == "end_chat":
        return "Alright, I’ll give you space. Take care of yourself, okay? 💜"

    # Mood-based fallback
    if mood == "positive":
        return "I'm glad you're feeling good! 😊 Keep it up!"
    elif mood == "negative":
        return "I'm here for you. Want to talk about it or try a calming tip?"
    else:
        return "Hmm, I sense you're neutral right now. Let's chat more if you like."
