from django.db import models


class User(models.Model):
    """
    Пользователь
    """
    class Meta:
        db_table = 'user'


class UserInfo(models.Model):
    class Meta:
        db_table = 'user_info'

    user = models.OneToOneField('integration_auth.User',
                                null=False,
                                default=None,
                                on_delete=models.CASCADE)
