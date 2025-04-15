import csv
from datetime import datetime
import os

log_file = 'mood_log.csv'

def log_interaction(user_input, mood, intent):
    # Check if file exists
    file_exists = os.path.isfile(log_file)

    with open(log_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write header if file is new
        if not file_exists:
            writer.writerow(["Timestamp", "User Input", "Mood", "Intent"])

        # Write the log entry
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), user_input, mood, intent])
