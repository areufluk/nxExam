from django.db import models

class subjectFilterModel(models.Model):
    id_exam = models.TextField()
    id_problem = models.TextField()
    problem = models.TextField()
    level = models.TextField()
    score_plus = models.IntegerField()
    score_sub = models.IntegerField()
    
    class Meta:
        db_table = 'question'
        managed = False