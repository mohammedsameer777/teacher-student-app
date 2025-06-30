from django.shortcuts import render
from django.contrib.auth import logout
from django.http import JsonResponse


def login_view(request):
    return render(request, "login.html")
    

def logout_view(request):
    logout(request)
    return JsonResponse({"message": "Logged out"})

def register_view(request):
    return render(request, "register.html")
    

def dashboard_view(request):
    return render(request, "dashboard.html")
