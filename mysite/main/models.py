from django.db import models
from datetime import datetime
from django.contrib.postgres.fields import JSONFielde
# Create your models here.


def get_milestones():
    return {""}


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    project_description = models.TextField()
    project_published = models.DateTimeField(
        'date published', default=datetime.now)
    milestones = JSONField(
        "QuarterlyMilestones", default=get_milestones)

    def __str__(self):
        return self.project_name
