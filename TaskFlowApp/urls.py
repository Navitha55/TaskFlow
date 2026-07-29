from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_page, name="index"),
    path("signin/", views.signIn, name="signIn"),
    path("signup/", views.signUp, name="signUp"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("forgot/",views.forgot, name="forgot"),
    path("logout/", views.logout_user, name="logout"),
]