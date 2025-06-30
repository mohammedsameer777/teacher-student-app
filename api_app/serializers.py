from rest_framework import serializers
from .models import Teacher, Student
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'email', 'name']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = Teacher
        fields = ['email', 'name', 'password']

    def create(self, validated_data):
        user = Teacher(
            email=validated_data['email'],
            name=validated_data['name']
        )
        user.set_password(validated_data['password'])  # hashes the password
        user.save()
        return user

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'grade']
