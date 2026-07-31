from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils import timezone
from .models import Task


def index_page(request):
    return render(request, "index.html")


def signIn(request):
    if request.method == "POST":
        email = request.POST.get("email", "").strip().lower()
        password = request.POST.get("password", "")
        user = authenticate(
            request,
            username=email,
            password=password
        )
        if user is not None:
            login(request, user)
            messages.success(
                request,
                f"Welcome back, {user.first_name or user.username}! 👋"
            )
            return redirect("dashboard")
        messages.error(
            request,
            "Invalid email or password."
        )
        return redirect("signIn")
    return render(
        request,
        "signin.html",
        {
            "active_form": "signin"
        }
    )


def signUp(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip().lower()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")
        if password != confirm_password:
            messages.error(
                request,
                "Passwords do not match."
            )
            return redirect("signUp")
        if User.objects.filter(username=email).exists():
            messages.error(
                request,
                "An account with this email already exists."
            )
            return redirect("signUp")
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )
        user.first_name = name
        user.save()
        messages.success(
            request,
            "Account created successfully! Please sign in."
        )
        return redirect("signIn")
    return render(
        request,
        "signin.html",
        {
            "active_form": "signup"
        }
    )

def forgot(req):
    if req.method == "POST":
        email = req.POST.get("email", "").strip().lower()
        password = req.POST.get("password", "")
        confirm_password = req.POST.get(
            "confirm_password",
            ""
        )
        if password != confirm_password:
            messages.error(
                req,
                "Passwords do not match."
            )
            return redirect("forgot")
        try:
            user = User.objects.get(
                email__iexact=email
            )
        except User.DoesNotExist:
            messages.error(
                req,
                "No account found with this email."
            )
            return redirect("forgot")
        user.set_password(password)
        user.save()


        messages.success(
            req,
            "Password changed successfully! Please sign in."
        )

        return redirect("signIn")
    return render(req,'forgot.html')


def dashboard(request):

    if not request.user.is_authenticated:
        return redirect("signIn")

    tasks = Task.objects.filter(
        user=request.user
    )

    total_tasks = tasks.count()

    completed_tasks = tasks.filter(
        status=True
    ).count()

    pending_tasks = tasks.filter(
        status=False
    ).count()

    if total_tasks > 0:
        completion_rate = round(
            (completed_tasks / total_tasks) * 100
        )
    else:
        completion_rate = 0

    today = timezone.localdate()

    today_tasks = tasks.filter(
        due_date=today
    ).order_by(
        "status",
        "due_date"
    )

    return render(
        request,
        "dashboard.html",
        {
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "pending_tasks": pending_tasks,
            "completion_rate": completion_rate,
            "today_tasks": today_tasks,
        }
    )

def my_tasks(request):

    if not request.user.is_authenticated:
        return redirect("signIn")

    tasks = Task.objects.filter(
        user=request.user
    ).order_by(
        "status",
        "due_date"
    )

    return render(
        request,
        "tasks.html",
        {
            "tasks": tasks
        }
    )

def create_task(request):
    if not request.user.is_authenticated:
        return redirect("signIn")
    
    if request.method == "POST":
        title = request.POST.get("title","").strip()
        description = request.POST.get("description","").strip()
        category = request.POST.get("category","daily")
        priority = request.POST.get("priority","medium")
        due_date = request.POST.get("due_date")
        reminder_datetime = request.POST.get("reminder_datetime")
        if not title:
            messages.error(
                request,
                "Task title is required."
            )
            return redirect("add_task")
        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            category=category,
            priority=priority,
            due_date=due_date,
            reminder_datetime=(reminder_datetime if reminder_datetime else None)
        )
        messages.success(
            request,
            "Task created successfully! ✅"
        )
        return redirect("my_tasks")
    
    return render(
        request,
        "add_task.html",
        {
            "category_choices": Task.CATEGORY_CHOICES,
            "priority_choices": Task.PRIORITY_CHOICES
        }
    )

def toggle_task(request, task_id):

    if not request.user.is_authenticated:
        return redirect("signIn")

    task = get_object_or_404(
        Task,
        id=task_id,
        user=request.user
    )

    if request.method == "POST":

        task.status = not task.status
        task.save()

    return redirect("my_tasks")

def edit_task(request, task_id):
    if not request.user.is_authenticated:
        return redirect("signIn")
    task = get_object_or_404(
        Task,
        id=task_id,
        user=request.user
    )
    if request.method == "POST":
        task.title = request.POST.get("title","").strip()
        task.description = request.POST.get("description","").strip()
        task.category = request.POST.get("category","daily")
        task.priority = request.POST.get("priority","medium")
        task.due_date = request.POST.get("due_date")
        reminder_datetime = request.POST.get(
            "reminder_datetime"
        )
        task.reminder_datetime = (reminder_datetime if reminder_datetime else None )
        task.save()
        messages.success(
            request,
            "Task updated successfully! ✏️"
        )
        return redirect("my_tasks")
    return render(
        request,
        "edit.html",
        {
            "task": task,
            "category_choices": Task.CATEGORY_CHOICES
        }
    )

def delete_task(request, task_id):

    if not request.user.is_authenticated:
        return redirect("signIn")
    task = get_object_or_404(
        Task,
        id=task_id,
        user=request.user
    )
    if request.method == "POST":
        task.delete()
        messages.success(
            request,
            "Task deleted successfully."
        )

    return redirect("my_tasks")

def calendar(request):

    if not request.user.is_authenticated:
        return redirect("signIn")

    tasks = Task.objects.filter(
        user=request.user
    ).order_by("due_date")

    return render(
        request,
        "calendar.html",
        {
            "tasks": tasks
        }
    )

def analytics(request):

    if not request.user.is_authenticated:
        return redirect("signIn")

    tasks = Task.objects.filter(
        user=request.user
    )

    total_tasks = tasks.count()

    completed_tasks = tasks.filter(
        status=True
    ).count()

    pending_tasks = tasks.filter(
        status=False
    ).count()

    high_priority = tasks.filter(
        priority="high"
    ).count()

    medium_priority = tasks.filter(
        priority="medium"
    ).count()

    low_priority = tasks.filter(
        priority="low"
    ).count()

    completion_rate = 0

    if total_tasks > 0:
        completion_rate = round(
            (completed_tasks / total_tasks) * 100
        )

    categories = {}

    for task in tasks:
        category = task.get_category_display()

        if category not in categories:
            categories[category] = 0

        categories[category] += 1

    return render(
        request,
        "analytics.html",
        {
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "pending_tasks": pending_tasks,
            "completion_rate": completion_rate,
            "high_priority": high_priority,
            "medium_priority": medium_priority,
            "low_priority": low_priority,
            "categories": categories,
        }
    )

def settings(request):

    if not request.user.is_authenticated:
        return redirect("signIn")

    user = request.user

    if request.method == "POST":

        name = request.POST.get(
            "name",
            ""
        ).strip()

        email = request.POST.get(
            "email",
            ""
        ).strip().lower()

        if not name:
            messages.error(
                request,
                "Name cannot be empty."
            )
            return redirect("settings")

        if not email:
            messages.error(
                request,
                "Email cannot be empty."
            )
            return redirect("settings")

        existing_user = User.objects.filter(
            email__iexact=email
        ).exclude(
            id=user.id
        ).first()

        if existing_user:
            messages.error(
                request,
                "This email is already being used."
            )
            return redirect("settings")

        user.first_name = name
        user.email = email
        user.username = email
        user.save()

        messages.success(
            request,
            "Profile updated successfully! ✅"
        )

        return redirect("settings")

    return render(
        request,
        "settings.html"
    )

def logout_user(request):
    logout(request)
    messages.success(
        request,
        "You have been logged out successfully."
    )
    return redirect("signIn")