from django import forms

from leads.models import Lead


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ("name", "phone", "message")
