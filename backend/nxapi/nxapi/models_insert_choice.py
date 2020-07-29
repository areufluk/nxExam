from django.db import models
from django.utils import timezone

class createChoiceModel(models.Model):
    id_problem = models.TextField()
    choice_text = models.TextField()
    IsTrue = models.BooleanField()
    class Meta:
        db_table = 'choice'
        managed = False