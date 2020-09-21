from django import forms
from .models import HigherStudiesN, ResearchNew

class CreateHigher_studies(forms.ModelForm):
    class Meta:
        model = HigherStudiesN
        fields = ['university', 'study_domain']

class Create_Research(forms.ModelForm):
    class Meta:
        model = ResearchNew
        fields = ['research_title', 'domain']