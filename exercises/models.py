from django.db import models
from muscle_groups.models import MuscleGroups
from django.core.validators import MinValueValidator, MaxValueValidator


category_choices = (
    ('Musculação', 'Musculação'),
    ('Cardio', 'Cardio'),
)
difficulty_level_choices = (
    ('Facíl', 'Facíl'),
    ('Intermediário', 'Intermediário'),
    ('Difícil', 'Difícil')
)


class Exercice(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=category_choices)
    muscle_groups = models.ManyToManyField(MuscleGroups, related_name='MuscleGroups')
    difficulty_level = models.CharField(max_length=255, choices=difficulty_level_choices)
    equipment = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
        blank=True,
        null=True,
    )
    photo = models.ImageField(upload_to='exercices/', blank=True, null=True)
    description = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
