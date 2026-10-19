from django.contrib import admin

from leads.models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "created_at")
    search_fields = ("name", "phone")
    date_hierarchy = "created_at"
    readonly_fields = ("name", "phone", "created_at", "message")

    def has_add_permission(self, request):
        return False
