from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import registrationView

urlpatterns=[
    path('', views.home, name='message'),
    path('register/', registrationView, name='register'),
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),

]