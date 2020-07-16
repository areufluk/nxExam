from django.db import models
from django.utils import timezone

class createProbModel(models.Model):
    id_exam = models.TextField()
    problem = models.TextField()
    level = models.TextField()
    score_plus = models.IntegerField()
    score_sub = models.IntegerField()
    class Meta:
        db_table = 'question'
        managed = False