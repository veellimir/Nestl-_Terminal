# Generated by Django 4.2.7 on 2024-03-16 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=150, verbose_name='Категории сотрудников')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='url категорий')),
            ],
            options={
                'verbose_name': 'Категорию',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Имя сотрудника')),
                ('photo', models.ImageField(upload_to='media/profile/%Y/%m/%d/', verbose_name='Изображения сотрудника')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='url сотрудника')),
                ('collected', models.IntegerField(blank=True, null=True, verbose_name='Собранно коробов')),
                ('transported', models.IntegerField(blank=True, null=True, verbose_name='Перевезено паллет')),
                ('discharge', models.IntegerField(blank=True, null=True, verbose_name='Выгружено машин')),
                ('shipment', models.IntegerField(blank=True, null=True, verbose_name='Загружено машин')),
                ('others', models.IntegerField(blank=True, null=True, verbose_name='Время перерывов')),
                ('time_employment', models.DateTimeField(auto_now_add=True, verbose_name='Дата трудоустройства')),
                ('is_public', models.BooleanField(default=True, verbose_name='Числится в штате')),
                ('employee_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.categoryemployee', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Сотрудника',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
    ]
