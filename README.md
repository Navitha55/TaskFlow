# TaskFlow 🚀

TaskFlow is a productivity-focused task management web application designed to help users organize their daily activities, manage deadlines, and build consistent productivity habits.

The project started as a simple To-Do List landing page and is gradually evolving into a complete Django-based task management application.

TaskFlow provides individual user accounts so that each user can securely manage their own tasks and productivity activities.

---

## 🌟 Current Progress

TaskFlow is being developed incrementally.

### ✅ Completed

- Responsive landing page
- TaskFlow introduction and feature sections
- About section
- Light/Dark theme support
- Authentication interface
- User registration
- User login
- User logout
- Django session-based authentication
- Password change / forgot-password functionality
- Password confirmation validation
- Unique email validation during registration
- Authentication messages for success and error states
- Protected dashboard access
- Environment variable configuration using `django-environ`
- MySQL database integration

### 🚧 In Development

- Task creation
- Task editing
- Task deletion
- Task completion tracking
- Custom task categories
- Task priorities
- Deadline management
- Reminder/notification system
- Productivity streaks
- Dashboard analytics
- User-specific task management

---

## ✨ Planned Features

### 📝 Task Management

Users will be able to:

- Create tasks
- Edit tasks
- Delete tasks
- Mark tasks as completed
- View pending and completed tasks

### 📂 Custom Categories

Users can create categories according to their needs, such as:

- Work
- Study
- Personal
- Fitness
- Projects

### ⏰ Deadline Reminders

Users will be able to assign deadlines to tasks and receive reminders for important activities.

### 🔥 Productivity Streaks

TaskFlow will encourage consistency by tracking daily task completion and maintaining productivity streaks.

### 📊 Dashboard Analytics

The dashboard will provide insights into productivity, including:

- Completed tasks
- Pending tasks
- Daily progress
- Completion statistics
- Productivity trends

---

## 🔐 Authentication

TaskFlow uses Django's built-in authentication system.

Current authentication functionality includes:

- User registration
- Secure password hashing
- User login
- User logout
- Password change
- Email uniqueness validation
- Password confirmation
- Session-based authentication
- Protected dashboard access

Each user's tasks will be associated with their authenticated account.

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
│   ├── migrations/
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
│   ├── forgot.html
│   └── dashboard.html
│
├── .env.example
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md