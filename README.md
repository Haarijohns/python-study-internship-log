# Python Study and Internship Log

A simple Python command-line application to track study sessions and internship learning progress.

## Features

- Add a study session with a topic, duration, learning notes, and project name.
- View all recorded study sessions.
- Calculate the total number of sessions and total study time.
- Validate user input and reject empty text or invalid durations.
- Save study sessions in a JSON file.
- Load previously saved sessions when the application starts.
- Handle missing or corrupted JSON files.

## Technologies Used

- Python 3.11
- JSON
- Git and GitHub

## Project Structure

```text
python-study-internship-log/
│
├── study_log.py
├── study_sessions.json
├── json_error_test.py
├── invalid_test.json
├── README.md
└── .gitignore
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Haarijohns/python-study-internship-log.git
```

### 2. Open the project directory

```bash
cd python-study-internship-log
```

### 3. Activate the virtual environment

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If you have not created the virtual environment yet:

```powershell
py -3.11 -m venv .venv
```

### 4. Run the application

```bash
python study_log.py
```

## Application Menu

```text
====== Python Study Log ======
1. Add a study session
2. View all study sessions
3. Exit
```

Choose an option to add a session, view saved sessions, or exit.

## Data Storage

The application uses Python's built-in `json` module to store study sessions in `study_sessions.json`.

- `json.load()` reads saved sessions.
- `json.dump()` writes updated sessions.
- Previously saved sessions remain available after restarting the application.

## Testing

The following manual tests have been performed:

| Test                        | Result                    |
| --------------------------- | ------------------------- |
| Add a study session         | Passed                    |
| View all sessions           | Passed                    |
| Reject invalid duration     | Passed                    |
| Reject empty text           | Passed                    |
| Calculate total study time  | Passed                    |
| Save sessions to JSON       | Passed                    |
| Load sessions after restart | Passed                    |
| Handle missing JSON file    | Implemented               |
| Handle corrupted JSON file  | Passed in a separate test |

## Learning Objectives

This project is part of my Python and Web Development learning roadmap.

It provides practical experience with:

- Python functions and modules
- Lists and dictionaries
- Loops and conditional statements
- Exception handling
- Input validation
- File handling
- JSON data serialization and deserialization

## Current Status

Python command-line application with JSON-based data persistence.

Future development will extend the project towards a web-based Study and Internship Tracker.

## Author

Haari Johns
