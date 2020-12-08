from account.models import Account

from .get_info_from_db import *

from project.get_info_from_db import *
from professionalInfo.get_info_from_db import *
from study_research.get_info_from_db import *

def showProfile(id):
    print(type(id))
    profile_info = getProfile(id)
    user_info = Account.objects.get(id=id)

    profession = getProfessionalInfo(id)
    project = getProject(id)
    research = getResearch(id)
    higher_studies = getHigherStudies(id)


    facebook = getFacebook(id)
    phone = getPhone(id)
    a_mail = getA_mail(id)
    github = getGithub(id)
    linkedin = getLinkedIn(id)

    
    context = {'info': profile_info,
                       'user':user_info.name,
                       'projects':project,
                       'researchs':research,
                       'professions':profession,
                        'facebook':facebook,
                       'phone':phone,
                       'a_mail':a_mail,
                       'github':github,
                       'linkedin':linkedin,
                       'higher_studies':higher_studies,
                       'flag':True
    }

    return context