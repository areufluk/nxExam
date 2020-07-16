from django.db import models
from django.utils import timezone

class subModel(models.Model):
    subject_id = models.CharField(max_length = 50)
    subject_name = models.CharField(max_length = 50)
    teacher_name = models.CharField(max_length = 30)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ('start_time',)
        db_table = 'exam'
        managed = False


    