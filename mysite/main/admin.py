from django.contrib import admin
from .models import Project, Event
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    fields = ["project_name",
              "project_published",
              "project_description",
              "milestones"]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }


class EventAdmin(admin.ModelAdmin):
    fields = ["event_quarter",
              "event_project"]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Event, EventAdmin)
