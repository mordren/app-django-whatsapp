# Generated by Django 4.1.2 on 2022-11-02 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wp', '0003_rename_sage_mensage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mensage',
            old_name='mensagem',
            new_name='mensage',
        ),
    ]
