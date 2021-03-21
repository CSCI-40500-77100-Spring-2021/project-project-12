"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from SE import views

urlpatterns = [
    path('', views.home_page),
    path('admin/', admin.site.urls),
    path('conveniote/index.html', views.home_page, name='home'),
    path('conveniote/course1.html', views.course1, name='course1'),
    path('conveniote/video.html', views.video, name='video'),
    path('conveniote/grades.html', views.grades, name='grades'),
    path('conveniote/notes.html', views.notes, name='notes'),
    path('conveniote/syllabus.html', views.syllabus, name='syllabus'),
]
