from django.db import models
from django.utils import timezone

class createSubModel(models.Model):
    teacher_name = models.TextField()
    created_by = models.TextField()
    # timestamp = models.TextField()
    subject_name = models.TextField()
    subject_id = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    easy = models.IntegerField()
    medium = models.IntegerField()
    hard = models.IntegerField()
    backward = models.IntegerField()
    scoring_method = models.IntegerField()
    show_score = models.IntegerField()

    # sub_id = models.IntegerField()
    # sub_name = models.CharField(max_length = 50)
    # sub_teacher = models.CharField(max_length = 50)
    # sub_start = models.DateTimeField()
    # sub_stop = models.DateTimeField()
    class Meta:
        db_table = 'exam'
        # db_table = 'detail'
        managed = False