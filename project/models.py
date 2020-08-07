from django.db import models
from userProfile.models import Profile
from workingSkills.models import Domain,Environment,ToolsAndTechnology

class Project(models.Model):
    project_title = models.CharField(max_length=100)
    domain = models.ManyToManyField(Domain)
    environment = models.ManyToManyField(Environment)
    tools_and_technology = models.ManyToManyField(ToolsAndTechnology)
    profile = models.ManyToManyField(Profile)
