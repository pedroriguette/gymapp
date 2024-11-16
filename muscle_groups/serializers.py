from rest_framework import serializers
from . import models


class MuscleGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MuscleGroups
        fields = '__all__'
