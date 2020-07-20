from django.contrib import admin
from .models import Profile
from .models import Domain
from .models import Country
from .models import HigherStudiesUniversity
from .models import HigherStudies
from .models import ToolsAndTechnology,Environment,Organization,ProfessionalInfo,Project,Research

# Register your models here.
admin.site.register(Profile)
admin.site.register(Domain)
admin.site.register(Country)
admin.site.register(HigherStudiesUniversity)
admin.site.register(HigherStudies)
admin.site.register(ToolsAndTechnology)
admin.site.register(Environment)
admin.site.register(Organization)
admin.site.register(ProfessionalInfo)
admin.site.register(Project)
admin.site.register(Research)