from django import forms

from leads.models import Lead


class LeadForm(forms.ModelForm):
    consent = forms.BooleanField(
        required=True,
        label="Согласие на обработку персональных данных",
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
    )

    class Meta:
        model = Lead
        fields = ("name", "phone", "message", "consent")
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"class": "form-control"}),
        }
