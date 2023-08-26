# Generated by Django 4.1.7 on 2023-04-26 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_alter_timetable_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.CharField(blank=True, error_messages={'blank': "Введіть значення до поля 'Електрона почта клієнта'"}, max_length=200),
        ),
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.CharField(blank=True, error_messages={'blank': "Введіть значення до поля 'Ім'я клієнта'"}, max_length=50),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(blank=True, error_messages={'blank': "Введіть значення до поля 'Прізвище клієнта'"}, max_length=50),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(blank=True, error_messages={'blank': "Введіть значення до поля 'Номер мобільного телефону клієнта'", 'max_length': 'Введено багато символів. Номер телефону має містити 13 символів'}, max_length=13),
        ),
    ]
