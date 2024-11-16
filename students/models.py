from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from users.models import CustomUser


class Student(models.Model):
    user = models.OneToOneField(CustomUser, verbose_name='Usuario', on_delete=models.CASCADE)
    full_name = models.CharField(verbose_name='Nome', max_length=255)
    birthday = models.DateField(verbose_name='Data de nascimento')
    phone_number = models.CharField(
        verbose_name='Número de telefone',
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="O número de telefone deve estar no formato: '+999999999'. Até 15 dígitos permitidos."
            )
        ]
    )
    objective = models.CharField(verbose_name='Objetivo', max_length=500)
    frequency = models.IntegerField(
        validators=[
            MinValueValidator(1, 'Escolha no Minimo 1 vez na semana'),
            MaxValueValidator(6, 'O maximo é 6 vezes na semana'),
        ]
    )
    active = models.BooleanField(verbose_name="Ativo")
    photo = models.ImageField(upload_to='students', verbose_name='Foto', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    updated_at = models.DateField(verbose_name='Atualizado em', auto_now=True)

    def __str__(self):
        return self.full_name

    def email(self):
        return self.user.email
