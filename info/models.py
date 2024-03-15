from django.db import models


class Info(models.Model):
    assembling = models.IntegerField(verbose_name='Кол-во коробов для сборки')
    transported_pallet = models.IntegerField(verbose_name='Перемещение паллет')
    coming_car = models.IntegerField(verbose_name='Выгрузка')
    out_car = models.IntegerField(verbose_name='Загрузка')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Информацию'
        verbose_name_plural = 'Информация'
