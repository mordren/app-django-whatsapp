# Generated by Django 4.1.2 on 2022-10-31 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0007_empresa_telefone_empresa_whatsapp'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoLaudo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Laudo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('dataValidade', models.DateField()),
                ('cliente', models.ManyToManyField(blank=True, null=True, to='clientes.person')),
                ('empresa', models.ManyToManyField(blank=True, null=True, to='clientes.empresa')),
                ('tipo', models.ManyToManyField(to='clientes.tipolaudo')),
            ],
        ),
    ]