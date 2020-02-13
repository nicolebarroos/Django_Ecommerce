from django.db import models
from django.core import validators
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        'Apelido/usuário', max_length=30, unique=True, validators=[validators.RegexValidator(
            regex = '^[\w.@+-]+$',
            message = ('Enter a valid value.'),
            code = 'invalid',
            inverse_match = False,
            flags = 0,
        )
        ],
        help_text='Um nome curto que será usado para identificá-lo de forma única na plataforma'
    
    )

    name = models.CharField('Nome', max_length=100, blank=True)
    email = models.EmailField('E-mail', unique=True)
    is_staff = models.BooleanField('Equipe', default=True)
    is_active = models.BooleanField('Ativo', default=True)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.name or self.username

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(" ")[0]
