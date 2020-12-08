from django.shortcuts import render
from django.db import connection

from account.models import Account
from .forms import UserProfile
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Profile

from .show_details_profile import *


@login_required(login_url= 'login')
def userProfileview(request):
    user = request.user
    try:
        existProfile = Profile.objects.get(profile_of=user)
        if existProfile:
            print(type(user))
            context = showProfile(user.id)

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


def viewPeople(request):
        profile = getAllPeople()
        return render(request, 'show all/show_people.html', {'profile':profile})

def profileDetails(request, id):

    context = showProfile(id)

    return render(request, 'show all/show_profile.html', context)

'''def my_custom_sql():
    with connection.cursor() as cursor:
        cursor.execute("SELECT name,batch,session from account_account,userProfile_profile where account_account.email = userProfile_profile.profile_of")
        row = cursor.fetchall()

    return row'''

