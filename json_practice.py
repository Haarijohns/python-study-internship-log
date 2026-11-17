import json
study_sessions = [
    {
        "topic": "Python Functions",
        "duration": 90,
        "notes": "Learned functions and return statements",
        "project": "Study Log"
    },
    {
        "topic": "Python Dictionaries",
        "duration": 60,
        "notes": "Learned dictionaries",
        "project": "Study Log"
    }
]

with open("study_sessions.json", "w", encoding="utf-8") as file:
    json.dump(study_sessions, file, indent=4)

print("Study sessions saved successfully!")
