# Generated by Django 3.1.1 on 2020-09-12 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200912_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.CharField(help_text='Enter field address', max_length=20, verbose_name='Адресс'),
        ),
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(help_text='Enter field age', verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='person',
            name='work',
            field=models.CharField(help_text='Enter field address', max_length=20, verbose_name='Работа'),
        ),
    ]
