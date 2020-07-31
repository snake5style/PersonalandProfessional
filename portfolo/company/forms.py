from django import forms
from company.models import Professional
# ceate a form
class ProfessionalForm(forms.ModelForm):
    # create a meta class
    class Meta:
        model = Professional
        fields = "__all__"
