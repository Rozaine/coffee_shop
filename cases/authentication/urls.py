from django.urls import path
from . import views

app_name = "authentication"

urlpatterns = [
    path("signup", views.signup, name="signup"),
    path("signin", views.signin, name="signin"),
    path("logout", views.logout, name="logout"),
    path("home", views.logout, name="logout"),
    path("profile", views.profile, name="profile"),
]