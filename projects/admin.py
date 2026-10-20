from django.contrib import admin

from projects.models import Project, ProjectImage, Review


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "service", "is_active")
    list_filter = ("service",)
    inlines = (ProjectImageInline,)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("author", "created_at", "is_active")
    list_filter = ("created_at",)
