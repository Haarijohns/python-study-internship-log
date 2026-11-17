import json
with open("study_sessions.json", "r", encoding="utf-8") as file:
    study_sessions = json.load(file)

print(type(study_sessions))

for session in study_sessions:
    print(f"Topic: {session['topic']}")
    print(f"Duration: {session['duration']} minutes")
    print(f"Project: {session['project']}")
    print("---------------------")