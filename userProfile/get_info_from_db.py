
from .models import *

def getProfile(user):
    try:
        profile_info = Profile.objects.get(profile_of=user)
        return profile_info

    except Profile.DoesNotExist:
        return "No profile"

def getAllPeople():
    try:
        profile = Profile.objects.all().select_related('profile_of')
        return profile
    except Profile.DoesNotExist:
        return "No People"

def getFacebook(user):
    try:
        facebook = Facebook.objects.get(profile=user)

        return facebook

    except Facebook.DoesNotExist:
        return 'You Have No Project'


def getPhone(user):
    try:
        phone = Phone.objects.get(profile=user)
        print(phone.phone_id)

        return phone

    except Phone.DoesNotExist:
        return 'You Have No Project'

def getA_mail(user):
    try:
        a_mail = AdditionalMail.objects.get(profile=user)

        return a_mail

    except AdditionalMail.DoesNotExist:
        return 'You Have No Project'


def getLinkedIn(user):
    try:
        linkedin = LinkedIn.objects.get(profile=user)

        return linkedin

    except LinkedIn.DoesNotExist:
        return 'You Have No Project'


def getGithub(user):
    try:
        github = Github.objects.get(profile=user)

        return github

    except Github.DoesNotExist:
        return 'You Have No Project'

