# Student Task & Internship Tracker – UI Sketch

## 1. Main Page Layout

The application will have a single main dashboard where users can create, view and manage their tasks.

The page will contain three main sections:

1. **Header:** Displays the application name, "Student Task & Internship Tracker".
2. **Add Task Section:** Contains a form for entering new task details.
3. **My Tasks Section:** Displays all existing tasks and provides options to manage them.

## 2. Add Task Form

The form will contain the following fields:

| Field      | Purpose                                       | Required? |
| ---------- | --------------------------------------------- | --------- |
| Task Title | Short description of the task                 | Yes       |
| Due Date   | Deadline for completing the task              | No        |
| Category   | Classification such as Academic or Internship | No        |

An **Add Task** button will submit the form.

The task title must not be empty. Invalid input should display a clear validation message.

## 3. Task List Layout

Below the form, the application will display a section titled "My Tasks".

Each task will display:

- Task title.
- Task status (Pending or Completed).
- Due date, if provided.
- Category, if provided.

Each task will have the following actions:

- Edit task details.
- Mark as complete or incomplete.
- Delete task after confirmation.

Tasks will initially be displayed using static sample data.

## 4. UI States

### 4.1 Normal State

When tasks are available:

- Display the task creation form.
- Display all existing tasks.
- Show each task's title, status, due date and category where available.
- Provide edit, completion and delete actions.

### 4.2 Empty State

When no tasks have been created:

- Keep the task creation form visible.
- Display the message: "No tasks yet. Add your first task!"
- Do not display sample task entries.

### 4.3 Invalid Input State

When a user tries to submit the form without entering a task title:

- Prevent the task from being added.
- Display the message: "Task title is required."
- Keep the user on the same page so they can correct the input.

## 5. Mobile Layout

The application should adapt to smaller screens.

On mobile devices:

- Display the application title at the top.
- Arrange form fields vertically.
- Make the Add Task button easy to tap.
- Display tasks one below another.
- Keep task actions accessible without horizontal scrolling.

The desktop layout may use more horizontal space, while the mobile layout will use a single-column structure.

## 6. Initial Design Approach

The first version will focus on a simple and understandable interface.

- Use clear headings and labels.
- Maintain consistent spacing between sections.
- Use readable text and appropriate button sizes.
- Distinguish Pending and Completed task statuses.
- Avoid unnecessary visual elements.

HTML will be used to create the page structure. CSS will be introduced to style the layout, and JavaScript will be added later to implement browser interactions.
