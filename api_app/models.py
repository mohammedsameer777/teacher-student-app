from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class TeacherManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("Teachers must have an email")
        teacher = self.model(email=self.normalize_email(email), name=name)
        teacher.set_password(password)
        teacher.save(using=self._db)
        return teacher

class Teacher(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)

    objects = TeacherManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

class Student(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=10)

    def __str__(self):
        return self.name

