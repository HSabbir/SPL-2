from django.conf import settings
from django.db import models
from workingSkills.models import Domain,Environment,ToolsAndTechnology
from account.models import Account



class Project(models.Model):

    project_title = models.CharField(max_length=100)
    domain = models.ManyToManyField(Domain)
    environment = models.ManyToManyField(Environment)
    tools_and_technology = models.ManyToManyField(ToolsAndTechnology)
    profile = models.ManyToManyField(Account)


class CreateProject(models.Model):
    project_title = models.CharField(max_length=100)
    domain = models.ManyToManyField(Domain)
    environment = models.ManyToManyField(Environment)
    tools_and_technology = models.ManyToManyField(ToolsAndTechnology)
    profile = models.ManyToManyField(Account)
    project_photo = models.ImageField(blank=True)

    def __str__(self):
        return self.project_title

