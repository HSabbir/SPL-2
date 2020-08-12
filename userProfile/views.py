from django.shortcuts import render
from .forms import UserProfile
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


@login_required(login_url= '/accounts/login/')
def userProfileview(request):
    user = request.user

    if request.method == 'POST':
        profile_form = UserProfile(data=request.POST)
        if profile_form.is_valid():
            instance = profile_form.save(commit=False)  # this is the trick.
            instance.user = request.user  # and this to get the currently logged in user
            instance.save()  # to commit the new info

            return HttpResponseRedirect('/')
        else:
            print(profile_form.errors)
    form = UserProfile
    context = {'form': form}

    return render(request,'userprofile.html', context)
