# Generated by Django 4.1.2 on 2022-11-01 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0017_laudo_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='laudo',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.empresa'),
        ),
    ]
