# Student Task & Internship Tracker – MVP Requirements

## 1. Project Overview

The Student Task & Internship Tracker is a web application designed to help university students and internship trainees organize responsibilities, manage tasks and monitor completion.

The initial version will focus on a simple, easy-to-use single-user experience.

## 2. Target Users

- University students managing assignments and academic responsibilities.
- Internship trainees managing assigned tasks, deadlines and activities.

## 3. User Stories

1. As a student or internship trainee, I want to create tasks so I can organize my responsibilities.
2. I want to view all my tasks so I can understand what needs attention.
3. I want to edit task details when requirements or deadlines change.
4. I want to mark tasks as complete or incomplete.
5. I want to delete unnecessary tasks after confirmation.
6. I want to see an empty-state message when I haven't created any tasks.

## 4. MVP Features

- Create tasks.
- View tasks.
- Edit tasks.
- Mark tasks complete/incomplete.
- Delete tasks with confirmation.
- Validate user inputs.
- Store tasks persistently using SQLite.
- Display loading, empty, success and error states.
- Support desktop and mobile layouts.

## 5. Task Data Fields

- ID: Unique task identifier.
- Title: A short description of the task.
- Status: Pending or completed.
- Due date: Optional deadline.
- Category: Optional task category.

## 6. Postponed Features

- Authentication and registration.
- Multiple-user support.
- Admin dashboard.
- Notifications and reminders.
- Calendar integration.
- Advanced analytics.
- AI-based recommendations.
- Cloud synchronization.

## 7. Acceptance Criteria

- Users can create tasks with non-empty titles.
- Users can view all tasks.
- Users can edit task details.
- Users can mark tasks complete or incomplete.
- Users must confirm before deleting tasks.
- Invalid input produces understandable feedback.
- Tasks persist after backend restart.
- An appropriate empty state appears when there are no tasks.

## 8. Initial Development Scope

The first frontend version will use static sample data. HTML will establish the structure, CSS will provide the layout, and JavaScript will introduce browser interactions in later modules.

Backend persistence, API integration and authentication will be introduced only in their scheduled roadmap stages.
