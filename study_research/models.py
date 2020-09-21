from django.db import models
from userProfile.models import Profile
from workingSkills.models import Domain
from account.models import Account


class Country(models.Model):
    country = models.CharField(max_length=40)

    def __str__(self):
        return self.country

class HigherStudiesUniversityN(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    university_name = models.CharField(max_length=150)

    def __str__(self):
        return self.university_name



class HigherStudiesN(models.Model):
    university = models.ForeignKey(HigherStudiesUniversityN, on_delete=models.CASCADE)
    profile = models.ForeignKey(Account, on_delete=models.CASCADE)
    study_domain = models.ManyToManyField(Domain)

class ResearchNew(models.Model):
    research_title = models.CharField(max_length=100)
    domain = models.ManyToManyField(Domain)
    profile = models.ManyToManyField(Account)

    def __str__(self):
        return self.research_title
