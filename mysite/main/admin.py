from django.contrib import admin
from .models import Project
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


admin.site.register(Project, ProjectAdmin)
