from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from leads.forms import LeadForm


class LeadCreateView(SuccessMessageMixin, CreateView):
    form_class = LeadForm
    template_name = "leads/lead_form.html"
    success_url = reverse_lazy("home")
    success_message = "Спасибо! Мы перезвоним вам в ближайшее время"
