from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import tasks
from tasks.models import Project, Task

class BugReport(models.Model):
    STATUS_CHOICES = [
        ('New', 'Новый'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершен'),
    ] 

    title = models.CharField(max_length=200)
    description = models.TextField()

    project = models.ForeignKey(
        Project,
        related_name='bugs',
        on_delete=models.CASCADE
    ) 
    task = models.ForeignKey(
        Task,
        related_name='bugs',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New',
    )

    priority = models.IntegerField(
        default=3,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
     )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FeatureRequest(models.Model):
    STATUS_CHOICES = [
        ('reviewing', 'Рассмотрение'),
        ('accepted', 'Принято'),
        ('rejected', 'Отклонено'),
    ] 

    title = models.CharField(max_length=200)
    description = models.TextField()

    project = models.ForeignKey(
        Project,
        related_name='freqs',
        on_delete=models.CASCADE
    ) 
    task = models.ForeignKey(
        Task,
        related_name='freqs',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='reviewing',
    )

    priority = models.IntegerField(
        default=3,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
     )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)