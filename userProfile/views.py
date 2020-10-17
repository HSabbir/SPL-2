from django.shortcuts import render
from django.db import connection

from account.models import Account
from .forms import UserProfile
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Profile
from project.views import viewProject
from study_research.views import viewResearch,viewHigherStudies
from professionalInfo.views import viewProfessionalInfo
from .contactInfoview import *

@login_required(login_url= 'login')
def userProfileview(request):
    user = request.user
    try:
        existProfile = Profile.objects.get(profile_of=user)
        if existProfile:

            #context = showProfile(request,user)

            user_info = existProfile.profile_of.name
            profile_info = Profile.objects.get(profile_of=user)

            profession = viewProfessionalInfo(request)
            project = viewProject(request)
            research = viewResearch(request)
            higher_studies = viewHigherStudies(request)


            facebook = viewFacebook(request)
            phone = viewPhone(request)
            a_mail = viewA_mail(request)
            github = viewGithub(request)
            linkedin = viewLinkedIn(request)

            q = showProfile(request,user)
            print(q)

            context = {'info': profile_info,
                       'user':user_info ,
                       'projects':project,
                       'researchs':research,
                       'professions':profession,
                        'facebook':facebook,
                       'phone':phone,
                       'a_mail':a_mail,
                       'github':github,
                       'linkedin':linkedin,
                       'higher_studies':higher_studies,
                       'flag':True
                       }

            return render(request, 'profile/viewProfile.html',context)

    except Profile.DoesNotExist:
        if request.method == 'POST':
            profile_form = UserProfile(data=request.POST)
            if profile_form.is_valid():
                instance = profile_form.save(commit=False)  # this is the trick.
                instance.profile_of = request.user  # and this to get the currently logged in user
                instance.save()  # to commit the new info

                return HttpResponseRedirect('/')
            else:
                print(profile_form.errors)
        form = UserProfile
        context = {'form': form}

        return render(request, 'profile/userprofile.html', context)


@login_required(login_url= 'login')
def showProfile(request,user):
    user_info = Account.get_full_name(user)
    profile_info = Profile.objects.get(profile_of=user)

    profession = viewProfessionalInfo(request)
    return profession
    '''project = viewProject(user)
    research = viewResearch(user)
    higher_studies = viewHigherStudies(user)

    facebook = viewFacebook(user)
    phone = viewPhone(user)
    a_mail = viewA_mail(user)
    github = viewGithub(user)
    linkedin = viewLinkedIn(user)

    context = {'info': profile_info,
               'user': user_info.name,
               'projects': project,
               'researchs': research,
               'professions': profession,
               'facebook': facebook,
               'phone': phone,
               'a_mail': a_mail,
               'github': github,
               'linkedin': linkedin,
               'higher_studies': higher_studies,
               'flag': True
               }

    return context'''


def viewPeople(request):

    try:
        profile = Profile.objects.all().select_related('profile_of')
        return render(request, 'show all/show_people.html', {'profile':profile})
    except Profile.DoesNotExist:
        return "No People"

'''def my_custom_sql():
    with connection.cursor() as cursor:
        cursor.execute("SELECT name,batch,session from account_account,userProfile_profile where account_account.email = userProfile_profile.profile_of")
        row = cursor.fetchall()

    return row'''

