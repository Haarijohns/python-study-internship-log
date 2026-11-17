study_session = {
    "topic": "Python Functions",
    "duration": 90,
    "notes": "Learned functions and return statements",
    "project": "Study Log",
    "date": "2026-11-06"
}
study_session["location"] = "Shimane, Japan"
study_session["duration"] = 120
study_session["project"] = "AI Engineer Roadmap"

del study_session["location"]
removed_date = study_session.pop("date")
print(removed_date)
print(study_session)
# print(f"Topic: {study_session['topic']}")
# print(f"Duration: {study_session['duration']} minutes")
# print(f"Learning notes: {study_session['notes']}")
# print(f"Project: {study_session['project']}")
# print(f"Date: {study_session['date']}")
# print(f"Duration data type: {type(study_session['duration']).__name__}")