from django.urls import path
from .views import *

urlpatterns = [
    path('create', createProject , name = 'create_project')
]