"""Todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from rest_framework.urlpatterns import format_suffix_patterns
from simple import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.goto),
    path('student/', views.studentlist.as_view(),name='student'),
    path('student/delete/', views.studentlist.as_view(),name='delete'),
    path('student/update/', views.studentlist.as_view(),name='delete'),
    # path('student/add/', views.studentlist.as_view(),name='add'),

]
# urlpatterns = format_suffix_patterns(urlpatterns)
