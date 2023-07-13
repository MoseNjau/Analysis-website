from django.urls import path
from . import views

app_name="users"
urlpatterns=[
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    path("profile/",views.ProfileView.as_view(), name="profile")
]