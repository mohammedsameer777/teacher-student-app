from django.urls import path
from .views import (
    RegisterView,
    CustomLoginView,
    ProfileView,
    StudentListCreateView,
    StudentDetailView
)

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("custom-login/", CustomLoginView.as_view()),
    path("profile/", ProfileView.as_view()),
    path("students/", StudentListCreateView.as_view()),
    path("students/<int:pk>/", StudentDetailView.as_view()),
]
