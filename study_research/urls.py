from django.urls import path
from .views import *

urlpatterns = [
    path('add_higher_studies/', createHigherStudies , name = 'add_higher_studies'),
    path('add_research/', createResearch , name = 'add_research')
]