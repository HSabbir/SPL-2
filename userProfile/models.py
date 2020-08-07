from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver


# user profile
class Profile(models.Model):
    IIT_PROGRAM = (
        ('BSSE', 'BSSE'),
        ('MSSE', 'MSSE'),
        ('MIT', 'MIT'),
        ('PGDIT', 'PGDIT'),
    )

    #this is my user profile model..i want a user will create model after login...i use model form before ...but need to specify user also login
    profile_of = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    session = models.CharField(max_length=20, blank=False, null=False )
    batch = models.IntegerField()  # batch = models.IntegerField(blank=False, null=False)
    iit_program = models.CharField(blank=True, choices=IIT_PROGRAM, max_length=10)
    college = models.CharField(max_length=50)
    graduate_university = models.CharField(max_length=50, default='Dhaka University')
    graduate_department = models.CharField(max_length=50, default='Software Engineering')
    photo = models.ImageField(blank=True)
    is_current = models.BooleanField(default=True)
    is_batchCoordinator = models.BooleanField(default=False)
    additional_mail = models.CharField(max_length=40,blank=True,null=True)
    facebook = models.CharField(max_length=250,null=True,blank=True)
    github = models.CharField(max_length=200,null=True,blank=True)
    phone = models.CharField(max_length=20,null=True,blank=True)
    linkedIn = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.profile_of.__str__()

    '''def save(self, *args, **kwargs):
        if not self.id:
        self.slug = slugify(self.title)

        return super(Profile, self).save(*args, **kwargs)'''


class Domain(models.Model):
    domain = models.CharField(max_length=30)

    def __str__(self):
        return self.domain

#Higher Studies
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


#skillset
class ToolsAndTechnology(models.Model):
    tools_and_technology = models.CharField(max_length=40)

    def __str__(self):
        return self.tools_and_technology


class Environment(models.Model):
    environment = models.CharField(max_length=40)

    def __str__(self):
        return self.environment

class Organization(models.Model):
    organization_name = models.CharField(max_length=40)
    organization_type = models.CharField(max_length=40)

    def __str__(self):
        return self.organization_name

class ProfessionalInfo(models.Model):
    designation = models.CharField(max_length=40, blank=True, null=True)
    organization_name = models.ForeignKey(Organization,on_delete=models.PROTECT)
    date_join = models.DateField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

#project

class Project(models.Model):
    project_title = models.CharField(max_length=100)
    domain = models.ManyToManyField(Domain)
    environment = models.ManyToManyField(Environment)
    tools_and_technology = models.ManyToManyField(ToolsAndTechnology)
    profile = models.ManyToManyField(Profile)


#class Research
class Research(models.Model):
    research_title = models.CharField(max_length=100)
    domain = models.ManyToManyField(Domain)
    profile = models.ManyToManyField(Profile)









