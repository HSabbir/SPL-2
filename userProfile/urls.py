from django.urls import path
from . import views

urlpatterns = [
    path('', views.userProfileview, name = 'userprofile.html')
]