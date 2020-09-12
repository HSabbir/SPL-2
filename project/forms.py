from django import forms

from .models import Project

class createProjectForm(forms.ModelForm):

    class Meta:

        model = Project
        fields = ('project_title', 'domain', 'environment', 'tools_and_technology')