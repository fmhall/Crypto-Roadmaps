from django.db import models
from datetime import datetime

# Create your models here.


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    project_description = models.TextField()
    project_published = models.DateTimeField(
        'date published', default=datetime.now)
    #milestones = JSONField()
    # milestones = models.ForeignKey()

    def __str__(self):
        return self.project_name

    # def get_milestones():
    #     out = {""}
    #     return out


class Event(models.Model):
    event_quarter = models.CharField(max_length=100)
    event_project = models.ForeignKey(Project, on_delete=models.CASCADE)

    # def get_event_name():
    #     event_name = event_project.objects.get()
