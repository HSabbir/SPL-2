from django.shortcuts import render
from .forms import UserProfile
from django.contrib.auth.decorators import login_required


@login_required(login_url= '/accounts/login/')
def userProfileview(request):
    useremail = request.user.email
    print(useremail)
    form = UserProfile(request.POST or None)
    if form.is_valid():
        form.save()
        UserProfile.profile_of = useremail

    context = {'form':form}

    return render(request,'userprofile.html', context)
