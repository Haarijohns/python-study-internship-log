import json

study_session = {
    "topic": "Python JSON",
    "duration": 60,
    "project": "Study Log"
}

json_text = json.dumps(study_session, indent=4)
print("JSON string")
print(json_text)

print(type(json_text))

python_data = json.loads(json_text)

print("\nConverted back into Python: ")
print(python_data)
print(type(python_data))
print(python_data["topic"])