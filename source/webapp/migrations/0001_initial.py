# Generated by Django 4.1.7 on 2023-02-20 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=150, verbose_name='Название категории')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(max_length=1000, null=True, verbose_name='Описание')),
                ('added_at', models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Стоимость')),
                ('image', models.TextField(max_length=3000, verbose_name='URL картинки')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='webapp.category', verbose_name='Категория')),
            ],
        ),
    ]