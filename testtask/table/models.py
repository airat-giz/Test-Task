from django.db import models


class Table(models.Model):
    date = models.CharField(verbose_name='Дата', max_length=2000, null=False, blank=False)
    title = models.CharField(verbose_name='Название', max_length=2000, null=False, blank=False)
    quantity = models.IntegerField(verbose_name='Количество', null=False, blank=False)
    distance = models.IntegerField(verbose_name='Расстояние', null=False, blank=False)
