from django.db import models
import tasks

class BugReport(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(
        tasks.Project,
        related_name='tasks',
        on_delete=models.CASCADE
    ) 
