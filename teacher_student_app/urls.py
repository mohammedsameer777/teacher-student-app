"""
URL configuration for teacher_student_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from frontend_app import views as frontend_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Frontend routes
    path('', frontend_views.login_view, name='login'),
    path('register/', frontend_views.register_view, name='register'),
    path('dashboard/', frontend_views.dashboard_view, name='dashboard'),
    path('logout/', frontend_views.logout_view, name='logout'),

    # Backend API
    path('api/', include('api_app.urls')),
]
