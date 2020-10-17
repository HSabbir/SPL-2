from django.shortcuts import render

from account.models import Account
from .forms import UserProfile
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import *
from project.views import viewProject
from study_research.views import viewResearch,viewHigherStudies


@login_required(login_url= 'login')
def viewFacebook(request):
    try:
        user = request.user
        facebook = Facebook.objects.get(profile=user)


        return facebook


    except Facebook.DoesNotExist:
        return 'You Have No Project'


@login_required(login_url='login')
def viewPhone(request):
    try:
        user = request.user
        phone = Phone.objects.get(profile=user)
        print(phone.phone_id)

        return phone


    except Phone.DoesNotExist:
        return 'You Have No Project'

@login_required(login_url='login')
def viewA_mail(request):
    try:
        user = request.user
        a_mail = AdditionalMail.objects.get(profile=user)


        return a_mail


    except AdditionalMail.DoesNotExist:
        return 'You Have No Project'


@login_required(login_url='login')
def viewLinkedIn(request):
    try:
        user = request.user
        linkedin = LinkedIn.objects.get(profile=user)

        return linkedin

    except LinkedIn.DoesNotExist:
        return 'You Have No Project'


@login_required(login_url='login')
def viewGithub(request):
    try:
        user = request.user
        github = Github.objects.get(profile=user)


        return github


    except Github.DoesNotExist:
        return 'You Have No Project'

