from django import forms
from .models import Profile

class UserProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['iit_program','batch','session','graduate_university','graduate_department','photo']