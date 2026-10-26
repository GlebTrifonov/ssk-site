from django.urls import path

from leads.views import LeadCreateView

urlpatterns = [path("lead/", LeadCreateView.as_view(), name="lead_create")]
