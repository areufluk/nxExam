from rest_framework import serializers
from .models import subModel

from .models_insert import createSubModel

from .models_insert_prob import createProbModel

class serializationClass(serializers.ModelSerializer):
    class Meta:
        model = subModel
        fields = ['subject_id','subject_name','teacher_name','start_time','end_time']

class createSubSerialize(serializers.ModelSerializer):
    class Meta:
        model = createSubModel
        fields = [
        'teacher_name',
        'created_by',
        'subject_name',
        'subject_id',
        'start_time',
        'end_time',
        'easy',
        'medium',
        'hard',
        'backward',
        'scoring_method',
        'show_score'
        ]

class createProbSerialize(serializers.ModelSerializer):
    class Meta:
        model = createProbModel
        fields = [
        'id_exam',
        'problem',
        'level',
        'score_plus',
        'score_sub'
        ]