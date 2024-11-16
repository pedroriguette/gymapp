from rest_framework import serializers
from . import models


class ExerciceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Exercice
        fields = '__all__'
