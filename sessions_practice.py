import json

def load_sessions():
    try:
        with open("study_sessions.json", "r", encoding="utf-8") as file:
            sessions = json.load(file)

        return sessions

    except FileNotFoundError:
        return []

def save_sessions(sessions):
    with open("study_sessions.json", "w", encoding="utf-8") as file:
        json.dump(sessions, file, indent=4)

study_sessions = load_sessions()

def get_valid_duration():
    while True:
        try:
            duration = int(input("Enter the study duration: "))
            if duration <= 0:
                print("Please enter a valid duration")
                continue

            return duration

        except ValueError:
            print("Invalid Duration!, Try Again")

def get_valid_text(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value
        print("This field cannot be empty. Please try again.")

def add_session(sessions):
    topic = get_valid_text("Enter the study topic: ")
    duration = get_valid_duration()
    notes = get_valid_text("What did you learn today? ")
    project = get_valid_text("Enter the project name: ")
    new_session = {
        "topic": topic,
        "duration": duration,
        "notes": notes,
        "project": project
    }
    sessions.append(new_session)

def list_sessions(sessions):
    total_duration = 0
    for session in sessions:
        print(f"Topic: {session['topic']}")
        print(f"Duration: {session['duration']} minutes")
        print(f"Learning notes: {session['notes']}")
        print(f"Project: {session['project']}")
        print("-------------------------")
        total_duration += session["duration"]
    return total_duration

def main():
    while True:
        print("\n====== Python Study Log ======")
        print("1. Add a study session")
        print("2. View all study sessions")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_session(study_sessions)
            save_sessions(study_sessions)
            print("Study session saved successfully!")

        elif choice == "2":
            total_duration = list_sessions(study_sessions)

            print(f"Total sessions: {len(study_sessions)}")
            print(f"Total study time: {total_duration} minutes")

        elif choice == "3":
            print("Thank you for using Python Study Log!")
            break
        else:
            print("Invalid choice. Please select 1,2 or 3.")

if __name__ == "__main__":
    main()
