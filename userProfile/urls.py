from django.urls import path
from . import views
from project.views import viewProject

urlpatterns = [
    path('', views.userProfileview, name='createprofile'),
    path('people/',views.viewPeople , name='view_all_people'),
    path('people/<int:id>/', views.profileDetails, name='profile_details')

]