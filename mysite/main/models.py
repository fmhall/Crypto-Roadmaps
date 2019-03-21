from django.db import models
from datetime import datetime
# Create your models here.


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    project_description = models.TextField()
    project_published = models.DateTimeField(
        'date published', default=datetime.now)

    def __str__(self):
        return self.project_name
