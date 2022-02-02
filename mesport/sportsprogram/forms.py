from django import forms

from mesport.sportsprogram.models import PersonInfo


class PersonInfo(forms.ModelForm):
    class Meta:
        model = PersonInfo
        widgets = {
            'Password': forms.PasswordInput(),
        }