from django.db import models

from integration_auth.models import User


class Achievement(models.Model):
    """
    Достижение
    """
    class Meta:
        db_table = 'achievement'


class AchievementInfo(models.Model):
    """
    Информация о достижении
    """
    class Meta:
        db_table = 'achievement_info'

    achievement = models.OneToOneField('achieve_management.Achievement',
                                       null=False,
                                       default=None,
                                       on_delete=models.CASCADE)


class UserAchievementInfo(models.Model):
    """
    Информация о прогрессе пользователя в достижении
    """
    class Meta:
        db_table = 'user_achievement_info'

    user_achievement = models.OneToOneField('achieve_management.UserAchievement',
                                            null=False,
                                            default=None,
                                            on_delete=models.CASCADE)


class UserAchievement(models.Model):
    """
    Мостовая таблица для связи пользователя, достижения и прогрессе пользователя в достижении
    """
    class Meta:
        db_table = 'user_achievement'
        unique_together = ('user', 'achievement',)

    user = models.ForeignKey('integration_auth.User',
                             null=False,
                             default=None,
                             on_delete=models.CASCADE)
    achievement = models.ForeignKey('achieve_management.Achievement',
                                    null=False,
                                    default=None,
                                    on_delete=models.CASCADE)

