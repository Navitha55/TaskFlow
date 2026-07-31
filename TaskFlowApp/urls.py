from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_page, name="index"),
    path("signin/", views.signIn, name="signIn"),
    path("signup/", views.signUp, name="signUp"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("forgot/",views.forgot, name="forgot"),
    path("logout/", views.logout_user, name="logout"),
    path("tasks/",views.my_tasks,name="my_tasks"),
    path("tasks/add/", views.create_task, name="add_task"),
    path("tasks/<int:task_id>/edit/",views.edit_task,name="edit_task"),
    path("tasks/<int:task_id>/delete/",views.delete_task,name="delete_task"),
    path("tasks/<int:task_id>/toggle/",views.toggle_task,name="toggle_task"),
    path("calendar/",views.calendar,name="calendar"),
    path("analytics/", views.analytics, name="analytics"),
    path("settings/", views.settings, name="settings"),
]