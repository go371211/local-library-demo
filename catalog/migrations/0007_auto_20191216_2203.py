# Generated by Django 3.0 on 2019-12-16 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20191215_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='birth'),
        ),
        migrations.AlterField(
            model_name='author',
            name='date_of_death',
            field=models.DateField(blank=True, null=True, verbose_name='died'),
        ),
    ]