from rest_framework import serializers
from . import models


class TrainingSheetSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TrainingSheet
        fields = [
            'id',
            'student',
            'coach',
            'exercice',
            'series',
            'repetitions',
            'time',
            'group',
            'created_at',
            'updated_at',
        ]
