from django.db import models

from core.mixins.choice_enum import ChoiceEnum


class User(models.Model):
    """
    Модель, описывающая пользователя
    """
    phone_number = models.CharField(max_length=64,
                                    null=True,
                                    blank=True)
    email = models.EmailField(max_length=256,
                              null=True,
                              blank=True)
    password = models.CharField(max_length=1024,
                                null=False,
                                blank=False)


class GroupRights(ChoiceEnum):
    DEFAULT = 1


class Group(models.Model):
    """
    Модель, описывающая группу пользователей по разделению прав
    """
    users = models.ManyToManyField(to=User,
                                   blank=True,
                                   related_name='groups',
                                   default=list())
    right = models.IntegerField(default=GroupRights.DEFAULT.value(),
                                choices=GroupRights.choices())
