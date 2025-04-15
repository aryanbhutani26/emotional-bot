import re

def detect_intent(user_input):
    user_input = user_input.lower()

    # 1. Venting
    if re.search(r"(hate myself|i'm worthless|i can't take it|i feel broken)", user_input):
        return 'venting'

    # 2. Seeking Help
    if re.search(r"(help me|what should i do|i need help|support)", user_input):
        return 'seeking_help'

    # 3. Asking for calming tips
    if re.search(r"(calming tip|relax|breathe|how to calm down)", user_input):
        return 'calming_tip'

    # 4. Expressing gratitude
    if re.search(r"(thank you|thanks|appreciate it|you helped)", user_input):
        return 'gratitude'

    # 5. Exit/close chat
    if re.search(r"(leave me alone|i’m done|go away)", user_input):
        return 'end_chat'

    return 'unknown'
