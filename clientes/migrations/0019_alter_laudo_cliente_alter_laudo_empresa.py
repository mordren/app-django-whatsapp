# Generated by Django 4.1.2 on 2022-11-02 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0018_laudo_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laudo',
            name='cliente',
            field=models.ForeignKey(blank=True, help_text='Se não tem cliente deixar vazio', null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.person'),
        ),
        migrations.AlterField(
            model_name='laudo',
            name='empresa',
            field=models.ForeignKey(blank=True, help_text='Se não tem empresa deixar vazio', null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.empresa'),
        ),
    ]