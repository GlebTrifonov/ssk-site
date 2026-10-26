from django.urls import reverse_lazy
from django.views.generic import CreateView

from leads.forms import LeadForm


class LeadCreateView(CreateView):
    form_class = LeadForm
    template_name = "leads/lead_form.html"
    success_url = reverse_lazy("home")
