from .models import CreateProject

def getProject(user):
    try:
        project = CreateProject.objects.filter(profile=user)

        return project

    except CreateProject.DoesNotExist:
        return 'You Have No Project'