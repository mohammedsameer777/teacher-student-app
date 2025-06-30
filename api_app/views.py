from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from .models import Student, Teacher
from .serializers import (
    RegisterSerializer,
    TeacherSerializer,
    StudentSerializer
)

# ✅ Register a new teacher and return a JWT token
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            teacher = serializer.save()
            token = RefreshToken.for_user(teacher)
            return Response({
                "token": str(token.access_token),
                "teacher": TeacherSerializer(teacher).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ✅ Login and return JWT
class CustomLoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(email=email, password=password)
        if user:
            token = RefreshToken.for_user(user)
            return Response({
                "token": str(token.access_token),
                "teacher": TeacherSerializer(user).data,
                "message": "Login successful"
            }, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

# ✅ Return the logged-in teacher’s profile
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(TeacherSerializer(request.user).data)

# ✅ List/Add students for current teacher
class StudentListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.filter(teacher=self.request.user)

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)

# ✅ View/Update/Delete individual student (only if owned by teacher)
class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.filter(teacher=self.request.user)
