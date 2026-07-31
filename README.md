# TaskFlow 🚀

TaskFlow is a productivity-focused task management web application built with Django. It helps users organize tasks, manage priorities and deadlines, and receive email reminders for important activities.

The project started as a simple To-Do List landing page and has gradually evolved into a complete Django-based task management application.

TaskFlow provides individual user accounts so that each user can securely manage their own tasks.

---

## 📌 Project Status

### Phase 1 — Completed ✅

The first development phase of TaskFlow has been successfully completed.

Phase 1 focused on building the core task management system, authentication, database integration, and task reminder functionality.

---

## 🌟 Phase 1 Features

### 🔐 Authentication

- User registration
- User login
- User logout
- Django session-based authentication
- Protected dashboard access
- Password change functionality
- Forgot-password functionality
- Password confirmation validation
- Unique email validation during registration
- Authentication success and error messages
- Session persistence using cookies

### 📝 Task Management

Users can:

- Create tasks
- Edit tasks
- Delete tasks
- Mark tasks as completed
- View pending and completed tasks
- Manage task descriptions
- Assign due dates
- Assign task priorities
- Assign task categories

### 📂 Task Categories

TaskFlow currently supports predefined categories such as:

- Daily
- Work
- Study
- Health
- Finance
- Shopping
- Personal
- Other

### 🎯 Task Priorities

Each task can have one of three priority levels:

- High
- Medium
- Low

### ⏰ Task Reminders

Users can assign a reminder date and time to a task.

TaskFlow includes an automated email reminder system that:

- Checks tasks whose reminder time has been reached
- Sends reminder emails to the user's registered email address
- Includes task information in the reminder email
- Prevents the same reminder from being sent repeatedly

### 🗄️ Database Integration

TaskFlow uses MySQL for storing:

- User accounts
- Tasks
- Categories
- Task priorities
- Task status
- Reminder information
- Task creation and update timestamps

### 🌐 Responsive UI

The application includes a responsive interface for:

- Desktop
- Tablet
- Mobile

The dashboard includes a persistent sidebar navigation and responsive task layouts.

---

## 🛠️ Technology Stack

### Frontend

- HTML5
- CSS3
- JavaScript

### Backend

- Python
- Django

### Database

- MySQL

### Authentication

- Django Authentication System
- Django Sessions
- Cookies

### Email

- Django Email Backend
- Gmail SMTP

### Environment Management

- django-environ

### Development Tools

- VS Code
- Git
- GitHub

---

## 📁 Project Structure

```text
TaskFlow/
│
├── TaskFlowApp/
│   ├── management/
│   │   └── commands/
│   │       └── send_task_reminders.py
│   │
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── TaskFlowProject/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── index.html
│   ├── signin.html
│   ├── signup.html
│   ├── forgot.html
│   ├── dashboard.html
│   ├── add_task.html
│   ├── edit_task.html
│   └── ...
│
├── .env.example
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md