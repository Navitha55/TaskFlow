from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


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
    return render(
        request,
        "dashboard.html"
    )


def logout_user(request):
    logout(request)
    messages.success(
        request,
        "You have been logged out successfully."
    )
    return redirect("signIn")