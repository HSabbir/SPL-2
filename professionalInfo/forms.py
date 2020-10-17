from django import forms

from .models import ProfessionalInfo


class CreateProfessionalInfo(forms.ModelForm):
    class Meta:
        model = ProfessionalInfo
        fields = ('designation', 'date_join', 'organization')
