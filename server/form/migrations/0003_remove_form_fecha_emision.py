# Generated by Django 4.2.3 on 2023-08-07 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_alter_form_fecha_emision'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='fecha_emision',
        ),
    ]