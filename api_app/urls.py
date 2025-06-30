from django.urls import path
from .views import (
    RegisterView,
    CustomLoginView,
    ProfileView,
    StudentListCreateView,
    StudentDetailView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('custom-login/', CustomLoginView.as_view(), name='custom-login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
]
