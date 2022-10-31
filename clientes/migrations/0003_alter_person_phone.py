# Generated by Django 4.1.2 on 2022-10-31 13:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_alter_person_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.PositiveBigIntegerField(help_text='DD-XXXX XXXX sem os espaços e sem o nove adicional', unique=True, validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]