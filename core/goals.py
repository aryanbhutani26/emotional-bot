import json
goals_file = "user_goals.json"

def save_goal_or_trigger(entry):
    try:
        with open(goals_file, "r") as f:
            data = json.load(f)
    except:
        data = {"goals": [], "triggers": []}

    if "goal:" in entry.lower():
        goal = entry.split("goal:")[1].strip()
        data["goals"].append(goal)
        msg = f"Got it! I've saved your goal: '{goal}' 🎯"
    elif "trigger:" in entry.lower():
        trigger = entry.split("trigger:")[1].strip()
        data["triggers"].append(trigger)
        msg = f"Thanks for sharing. I'll remember your trigger: '{trigger}' ⚠️"
    else:
        return "Try using: `goal: ...` or `trigger: ...` so I can store it."

    with open(goals_file, "w") as f:
        json.dump(data, f, indent=4)
    return msg

def view_goals_and_triggers():
    try:
        with open(goals_file, "r") as f:
            data = json.load(f)
        goals = "\n".join(f"• {g}" for g in data.get("goals", [])) or "No goals yet"
        triggers = "\n".join(f"• {t}" for t in data.get("triggers", [])) or "No triggers yet"
        return f"🎯 Your Goals:\n{goals}\n\n⚠️ Your Triggers:\n{triggers}"
    except:
        return "Nothing saved yet!"
