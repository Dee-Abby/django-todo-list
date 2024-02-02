from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Task(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  date_created = models.DateTimeField(default=timezone.now)
  deadline = models.DateTimeField(blank=True, null=True)


  class Meta:
    ordering = ['-date_created']


  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse("task_detail", kwargs={'pk' : self.pk})