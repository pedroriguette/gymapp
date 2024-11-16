from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O email deve ser passado')
        email = self.normalize_email(email)
        user = self.model(username=username.strip(), email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Um superuser deve ser is_staff=True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Um superuser deve ser is_superuser=True')

        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    USER_TYPER_CHOICES = (
        ('student', 'Student'),
        ('coach', 'Coach'),
    )

    user_type = models.CharField(max_length=20, choices=USER_TYPER_CHOICES)

    username = models.CharField(
        max_length=150,
        unique=True,
        help_text='O maximo de caracteres é 150',
        validators=[],
        error_messages={
            'unique': "a user with that name already exists."
        },
    )

    def is_student(self):
        return self.user_type == 'student'

    def is_coach(self):
        return self.user_type == 'coach'

    objects = CustomUserManager()
