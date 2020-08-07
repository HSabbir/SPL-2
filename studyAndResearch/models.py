from django.db import models
from userProfile.models import Profile
from workingSkills.models import Domain

class HigherStudiesUniversity(models.Model):
    university_name = models.CharField(max_length=150)

    def __str__(self):
        return self.university_name

class Country(models.Model):
    country = models.CharField(max_length=40)

    def __str__(self):
        return self.country

class HigherStudies(models.Model):
    university_name = models.ForeignKey( HigherStudiesUniversity,on_delete = models.CASCADE )
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    study_domain = models.ForeignKey(Domain,on_delete=models.CASCADE)

class Research(models.Model):
    research_title = models.CharField(max_length=100)
    domain = models.ManyToManyField(Domain)
    profile = models.ManyToManyField(Profile)
