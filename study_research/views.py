from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import CreateHigher_studies,Create_Research
from .models import ResearchNew,HigherStudiesN
from account.models import Account

@login_required(login_url= 'login')
def createHigherStudies(request):
    form = CreateHigher_studies()
    #print(request.user)
    if request.method == 'POST':
        form = CreateHigher_studies(request.POST or None)

        if form.is_valid():
            '''id = request.user
            user = Account.objects.filter(profile_of=request.user)'''
            instance = form.save(commit=False)  # this is the trick.
            instance.profile = request.user  # and this to get the currently logged in user
            instance.save()


            return HttpResponseRedirect(redirect_to='/userprofile/')
    form = CreateHigher_studies

    return render(request, 'study_and_reserach/create_study_and_research.html', {'form': form, 'title':'Add HigherStudies'})


@login_required(login_url= 'login')
def createResearch(request):
    form = Create_Research()
    #print(request.user)
    if request.method == 'POST':
        form = Create_Research(request.POST or None)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            user = Account.objects.get(email=request.user.email)

            instance.profile.add(user)
            instance.save()


            return HttpResponseRedirect(redirect_to='/userprofile/')
    form = Create_Research

    return render(request, 'study_and_reserach/create_study_and_research.html', {'form': form, 'title':'Add Research'})


@login_required(login_url= 'login')
def viewResearch(request):
    try:
        user = request.user
        research = ResearchNew.objects.filter(profile=user)

        return research
        #return render(request, 'profile/viewProfile.html', {'projects':project})

    except ResearchNew.DoesNotExist:
        return 'You Have No Research'
        #return render(request,'profile/viewProfile.html',{'project_not_exist':'You Have No Project'})'''

@login_required(login_url= 'login')
def viewHigherStudies(request):
    try:
        user = request.user
        higherStudies = HigherStudiesN.objects.filter(profile=user)

        return higherStudies
        #return render(request, 'profile/viewProfile.html', {'projects':project})

    except HigherStudiesN.DoesNotExist:
        return 'You Have not added Higher Studies'
        #return render(request,'profile/viewProfile.html',{'project_not_exist':'You Have No Project'})'''
