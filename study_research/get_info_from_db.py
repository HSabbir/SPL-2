from .models import *

def getResearch(user):
    try:
        research = ResearchNew.objects.filter(profile=user)

        return research

    except ResearchNew.DoesNotExist:
        return 'You Have No Research'


def getHigherStudies(user):
    try:
        higherStudies = HigherStudiesN.objects.filter(profile=user)

        return higherStudies

    except HigherStudiesN.DoesNotExist:
        return 'You Have not added Higher Studies'