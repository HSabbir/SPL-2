from django.db import models
from django.conf import settings
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
    session = models.CharField(max_length=20, blank=False, null=True )
    batch = models.IntegerField(null=True)  # batch = models.IntegerField(blank=False, null=False)
    iit_program = models.CharField(blank=True, choices=IIT_PROGRAM, max_length=10)
    college = models.CharField(max_length=50,null=True)
    graduate_university = models.CharField(max_length=50, default='Dhaka University')
    graduate_department = models.CharField(max_length=50, default='Software Engineering')
    photo = models.ImageField(blank=True)
    is_current = models.BooleanField(default=True)
    is_batchCoordinator = models.BooleanField(default=False)

    def __str__(self):
        return str(self.profile_of)

'''@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_for_new_user(sender, created, instance, **kwargs):
    if created:
        profile = Profile(profile_of=instance)
        profile.save()'''


class Contact(models.Model):
    Profile = models.ForeignKey(Profile,on_delete = models.CASCADE)
    additional_mail = models.CharField(max_length=40, blank=True, null=True)
    facebook = models.CharField(max_length=250, null=True, blank=True)
    github = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    linkedIn = models.CharField(max_length=100, null=True, blank=True)









