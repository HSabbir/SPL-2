from django.urls import path
from .views import *

urlpatterns = [
    path('add_professional_info', createProfessionalInfo , name = 'add_professional_info')
]