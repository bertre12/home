from django.db import models
# from django.contrib.auth.models import User


class Human(models.Model):
    name = models.CharField(max_length=255, null=False, verbose_name='Имя')
    apartment = models.CharField(max_length=10, null=False, verbose_name='Номер квартиры')
    phone = models.CharField(max_length=20, null=False, verbose_name='Номер телефона')
    email = models.EmailField(max_length=255, null=False, verbose_name='Электронная почта')
    settling = models.DateField(auto_now_add=True, verbose_name='Дата заселения')

    def __str__(self):
        return self.name
