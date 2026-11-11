from django import forms

from leads.models import Lead


class LeadForm(forms.ModelForm):
    consent = forms.BooleanField(
        required=True,
        label="Согласие на обработку персональных данных",
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
    )
    website = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"class": "d-none", "autocomplete": "off", "tabindex": "-1"}
        ),
    )

    class Meta:
        model = Lead
        fields = ("name", "phone", "message", "consent")
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"class": "form-control"}),
        }

    def clean_website(self):
        value = self.cleaned_data["website"]
        if value:
            raise forms.ValidationError(
                "Не удалось отправить заявку. Попробуйте ещё раз."
            )
        return value
