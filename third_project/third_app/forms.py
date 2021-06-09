from django import forms
from django.core import validators
from third_app import models

class PeopleForm(forms.ModelForm):
    class Meta:
        model = models.People
        fields = "__all__"

class job_form(forms.ModelForm):
    """docstring for job_form."""

    class Meta:
        model = models.Job
        fields = "__all__"
