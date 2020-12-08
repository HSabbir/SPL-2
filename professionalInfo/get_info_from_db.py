from .models import ProfessionalInfo

def getProfessionalInfo(user):
    try:
        professional_info = ProfessionalInfo.objects.filter(profile=user).order_by('date_join').reverse()

        return professional_info

    except ProfessionalInfo.DoesNotExist:
        return 'You Have No ProfessionalInfo'