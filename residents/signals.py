from django.contrib.auth.models import User
from .models import Human
from django.db.models.signals import post_save
from django.db.models.signals import pre_delete
from django.dispatch import receiver


# При создании новой записи.
@receiver(post_save, sender=Human)
def on_create(sender, instance, created, **kwargs):
    print('Запись создана.')


# При удалении записи.
@receiver(pre_delete, sender=Human)
def on_delete(sender, instance, **kwargs):
    print('Запись удалена.')


# При добавлении нового суперпользователя.
@receiver(post_save, sender=User)
def on_superuser_create(sender, instance, created, **kwargs):
    print('Новый суперпользователь.')
