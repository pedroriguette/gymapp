from django.db import models
from multiselectfield import MultiSelectField
from django.core.validators import RegexValidator
from users.models import CustomUser


working_days_choices = [
    ('SEG', 'Segunda-feira'),
    ('TER', 'Terça-feira'),
    ('QUA', 'Quarta-feira'),
    ('QUI', 'Quinta-feira'),
    ('SEX', 'Sexta-feira'),
    ('SAB', 'Sábado'),
    ('DOM', 'Domingo'),
]


status_choices = (
    ('AT', 'Ativo'),
    ('IN', 'Inativo'),
    ('FE', 'Férias'),
)


class Coach(models.Model):
    user = models.OneToOneField(CustomUser, verbose_name='Usuário', on_delete=models.CASCADE)
    full_name = models.CharField(verbose_name="Nome", max_length=255)
    birthday = models.DateField(verbose_name='Data de nascimento')
    phone_number = models.CharField(
        verbose_name='Número de Telefone',
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="O número de telefone deve estar no formato: '+999999999'. Até 15 dígitos permitidos."
            )
        ]
    )
    specialty = models.CharField(verbose_name='Especialidade', max_length=255, null=True, blank=True)
    entry = models.DateField(verbose_name='Dia da contratação')
    start_job = models.TimeField(verbose_name='Horario de inicio de expediente')
    ends_job = models.TimeField(verbose_name='Horario do fim do expediente')
    working_days = MultiSelectField(choices=working_days_choices)
    status = models.CharField(max_length=50, choices=status_choices)
    created_at = models.DateField(verbose_name='Criado em', auto_now_add=True)
    updated_at = models.DateField(verbose_name='Atualizado em', auto_now=True)

    def __str__(self):
        return self.full_name

    def email(self):
        return self.user.email
