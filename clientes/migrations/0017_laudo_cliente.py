# Generated by Django 4.1.2 on 2022-11-01 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0016_alter_laudo_numero'),
    ]

    operations = [
        migrations.AddField(
            model_name='laudo',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.person'),
        ),
    ]
