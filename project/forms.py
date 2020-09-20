from django import forms

from .models import CreateProject

class createProjectForm(forms.ModelForm):

    class Meta:

        model = CreateProject
        fields = ('project_title', 'domain', 'environment', 'tools_and_technology','project_photo')