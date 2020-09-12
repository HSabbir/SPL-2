from django.conf import settings
from django.db import models
from workingSkills.models import Domain,Environment,ToolsAndTechnology

class Project(models.Model):
    profile_of = models.ManyToManyField(settings.AUTH_USER_MODEL, null=False)
    project_title = models.CharField(max_length=100)
    domain = models.ManyToManyField(Domain)
    environment = models.ManyToManyField(Environment)
    tools_and_technology = models.ManyToManyField(ToolsAndTechnology)

