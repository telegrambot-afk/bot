from django.db import models


# Create your models here.


class User(models.Model):
    LANG_CHOICES = (
        ('en', 'English'),
        ('ru', 'Russian'),
        ('uz', 'Uzbek'),
    )
    tg_id = models.BigIntegerField(unique=True, blank=True, null=True)
    lang = models.CharField(max_length=2, choices=LANG_CHOICES, null=True, blank=True)
