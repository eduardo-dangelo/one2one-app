from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=120)
    created_at = models.DateTimeField('created at', default=timezone.now)

    def __str__(self):
        return self.title


class One2One(models.Model):
    title = models.CharField(max_length=120) 
    created_at = models.DateTimeField('created at', default=timezone.now)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Okr(models.Model):
    title = models.CharField(max_length=120)
    created_at = models.DateTimeField('created at', default=timezone.now)
    description = models.TextField(null=True, blank=True)
    result_note = models.TextField(null=True, blank=True)
    completion_score = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
     )
    one2one = models.ForeignKey(One2One, on_delete=models.CASCADE)

    def __str__(self):
        return self.title