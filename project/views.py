from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import createProjectForm
from .models import Project


@login_required(login_url= 'login')
def createProject(request):
    form = createProjectForm()
    user = request.user
    if request.method == 'POST':
        form = createProjectForm(data=request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.profile.set(user)
            instance.save()

            return HttpResponseRedirect('createprofile')
    form = createProjectForm
    context = {'form': form}

    return render(request, 'project/create_project.html', context)
