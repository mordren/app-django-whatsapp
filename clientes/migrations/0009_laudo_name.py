# Generated by Django 4.1.2 on 2022-10-31 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0008_tipolaudo_laudo'),
    ]

    operations = [
        migrations.AddField(
            model_name='laudo',
            name='name',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]