from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import ProfessionalInfo
from account.models import Account
from .forms import CreateProfessionalInfo
from .get_info_from_db import *


@login_required(login_url= 'login')
def createProfessionalInfo(request):
    form = CreateProfessionalInfo()
    #print(request.user)
    if request.method == 'POST':
        form = CreateProfessionalInfo(request.POST or None)

        if form.is_valid():
            '''id = request.user
            user = Account.objects.filter(profile_of=request.user)'''
            instance = form.save(commit=False)  # this is the trick.
            instance.profile = request.user  # and this to get the currently logged in user
            instance.save()


            return HttpResponseRedirect(redirect_to='/userprofile/')
    form = CreateProfessionalInfo
    context = {'form': form,'title':'Add Professional Information'}

    return render(request, 'study_and_reserach/create_study_and_research.html', context)



@login_required(login_url= 'login')
def viewProfessionalInfo(request):
    try:
        user = request.user
        professional_info = ProfessionalInfo.objects.filter(profile=user).order_by('date_join').reverse()

        return professional_info

    except ProfessionalInfo.DoesNotExist:
        return 'You Have No Project'


