from rest_framework import serializers
from . import models


class CoachSerializer(serializers.ModelSerializer):
    working_days = serializers.ListField()

    class Meta:
        model = models.Coach
        fields = [
            'id',
            'user',
            'full_name',
            'birthday',
            'phone_number',
            'specialty',
            'entry',
            'start_job',
            'ends_job',
            'working_days',
            'created_at',
            'updated_at',
        ]
