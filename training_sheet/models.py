from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from students.models import Student
from coaches.models import Coach
from exercises.models import Exercice


class Group(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='group', blank=True, null=True)

    def __str__(self):
        return self.name


class TrainingSheet(models.Model):
    student = models.ForeignKey(Student, verbose_name="Aluno", on_delete=models.CASCADE)
    coach = models.ForeignKey(
        Coach,
        verbose_name="Treinador",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    exercice = models.ForeignKey(
        Exercice,
        verbose_name="Exercicio",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    series = models.IntegerField(
        verbose_name='Series',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(50),
        ]
    )
    repetitions = models.IntegerField(
        verbose_name='Repetições',
        validators=[
            MinValueValidator(1, 'Adicione no maximo uma repetição'),
            MaxValueValidator(50, 'É permitido no maximo 50 repetições'),
        ]
    )
    time = models.IntegerField(
        verbose_name='Tempo de descanso',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(60),
        ]
    )
    group = models.ForeignKey(Group, max_length=255, on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

    def __str__(self):
        return self.student.full_name

    def photo(self):
        return self.exercice.photo
