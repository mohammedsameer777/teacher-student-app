from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Student
from .serializers import (
    RegisterSerializer,
    TeacherSerializer,
    StudentSerializer
)

# Register a new teacher and return JWT
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            teacher = serializer.save()
            token = RefreshToken.for_user(teacher)
            return Response({
                'token': str(token.access_token),
                'teacher': TeacherSerializer(teacher).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Return current teacher profile
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(TeacherSerializer(request.user).data)

# Add and list students
class StudentListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.filter(teacher=self.request.user)

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)  # ✅ This connects student to logged-in teacher

# View, Update, Delete specific student
class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.filter(teacher=self.request.user)
