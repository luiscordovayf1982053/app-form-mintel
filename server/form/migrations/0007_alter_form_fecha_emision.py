# Generated by Django 4.2.3 on 2023-08-07 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0006_alter_form_fecha_emision'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='fecha_emision',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
