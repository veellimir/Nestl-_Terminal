from django.db import models
from django.urls import reverse


class Profile(models.Model):
    """Модель связанна с моделью 'категория сотрудников'"""
    name = models.CharField(max_length=60, verbose_name='Имя сотрудника')
    photo = models.ImageField(upload_to='media/profile/%Y/%m/%d/', verbose_name='Изображения сотрудника')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='url сотрудника')

    collected = models.IntegerField(blank=True, null=True, verbose_name='Собранно коробов')
    transported = models.IntegerField(blank=True, null=True, verbose_name='Перевезено паллет')
    discharge = models.IntegerField(blank=True, null=True, verbose_name='Выгружено машин')
    shipment = models.IntegerField(blank=True, null=True, verbose_name='Загружено машин')
    others = models.IntegerField(blank=True, null=True, verbose_name='Время перерывов')

    time_employment = models.DateTimeField(auto_now_add=True, verbose_name='Дата трудоустройства')
    is_public = models.BooleanField(default=True, verbose_name='Числится в штате')
    employee_category = models.ForeignKey('CategoryEmployee', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('user_profile', kwargs={'user_slug': self.slug})

    class Meta:
        verbose_name = 'Сотрудника'
        verbose_name_plural = 'Сотрудники'


class CategoryEmployee(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='Категории сотрудников')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='url категорий')

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('category_employee', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
