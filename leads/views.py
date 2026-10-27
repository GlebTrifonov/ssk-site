from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from leads.forms import LeadForm
from leads.telegram import send_telegram_message


class LeadCreateView(SuccessMessageMixin, CreateView):
    form_class = LeadForm
    template_name = "leads/lead_form.html"
    success_url = reverse_lazy("home")
    success_message = "Спасибо! Мы перезвоним вам в ближайшее время"

    def form_valid(self, form):
        response = super().form_valid(form)
        text = f"Новая заявка\nИмя: {self.object.name}\nТелефон: {self.object.phone}\nЧто сделать: {self.object.message}"
        send_telegram_message(text)
        return response
