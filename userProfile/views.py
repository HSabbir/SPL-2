from django.shortcuts import render

from account.models import Account
from .forms import UserProfile
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Profile

@login_required(login_url= 'login')
def userProfileview(request):
    user = request.user
    try:
        existProfile = Profile.objects.get(profile_of=user)
        print(existProfile)
        if existProfile:
            user_info = Account.get_full_name(request.user)
            print(user_info)
            profile_info = Profile.objects.get(profile_of=user)
            print(profile_info.photo)

            return render(request, 'profile/viewProfile.html',{'info': profile_info,'user':user_info})

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
