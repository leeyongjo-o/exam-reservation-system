# Generated by Django 5.1.1 on 2024-09-19 21:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='participants',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(50000)], verbose_name='응시인원'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.IntegerField(choices=[(0, '대기중'), (1, '확정됨')], default=0, verbose_name='예약 상태'),
        ),
    ]
