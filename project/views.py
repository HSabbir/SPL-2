from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import createProjectForm
from .models import CreateProject
from account.models import Account

@login_required(login_url= 'login')
def createProject(request):
    form = createProjectForm()
    #print(request.user)
    if request.method == 'POST':
        form = createProjectForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            '''id = request.user
            user = Account.objects.filter(profile_of=request.user)'''
            instance = form.save(commit=False)
            instance.save()
            user = Account.objects.get(email=request.user.email)

            instance.profile.add(user)
            instance.save()


            return HttpResponseRedirect(redirect_to='/userprofile/')
    form = createProjectForm
    context = {'form': form,'title':'Create Project'}

    return render(request, 'project/create_project.html', context)

@login_required(login_url= 'login')
def viewProject(request):
    try:
        user = request.user
        project = CreateProject.objects.filter(profile=user)
        '''list = []
        for i in project:
            list.append(i)'''

        return project
        #return render(request, 'profile/viewProfile.html', {'projects':project})

    except CreateProject.DoesNotExist:
        return 'You Have No Project'
        #return render(request,'profile/viewProfile.html',{'project_not_exist':'You Have No Project'})
