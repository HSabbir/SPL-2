from django.db import models


class ToolsAndTechnology(models.Model):
    tools_and_technology = models.CharField(max_length=40)

    def __str__(self):
        return self.tools_and_technology


class Environment(models.Model):
    environment = models.CharField(max_length=40)

    def __str__(self):
        return self.environment

class Domain(models.Model):
    domain = models.CharField(max_length=30)

    def __str__(self):
        return self.domain

