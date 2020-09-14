from django.urls import path
from . import views
from project.views import viewProject

urlpatterns = [
    path('', views.userProfileview, name='createprofile'),


]