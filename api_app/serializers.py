from rest_framework import serializers
from .models import Teacher, Student
from django.contrib.auth import authenticate

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'email', 'name']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['email', 'name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return Teacher.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user:
            return user
        raise serializers.ValidationError("Invalid credentials")

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'grade']  
