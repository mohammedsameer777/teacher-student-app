from django.contrib.auth.backends import ModelBackend
from .models import Teacher

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = Teacher.objects.get(email=email)
            if user.check_password(password):
                return user
        except Teacher.DoesNotExist:
            return None
