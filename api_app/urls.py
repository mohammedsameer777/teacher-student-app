from django.urls import path
from .views import RegisterView, ProfileView, StudentListCreateView, StudentDetailView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('students/', StudentListCreateView.as_view()),  # ✅ FIXED
    path('students/<int:pk>/', StudentDetailView.as_view()),  # ✅
]
    