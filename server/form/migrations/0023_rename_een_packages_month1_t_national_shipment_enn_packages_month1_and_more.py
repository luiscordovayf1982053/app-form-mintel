# Generated by Django 4.2.3 on 2023-09-05 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0022_rename_number_docs_t_national_shipment_een_packages_month1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='t_national_shipment',
            old_name='een_packages_month1',
            new_name='enn_packages_month1',
        ),
        migrations.RenameField(
            model_name='t_national_shipment',
            old_name='een_packages_month2',
            new_name='enn_packages_month2',
        ),
        migrations.RenameField(
            model_name='t_national_shipment',
            old_name='een_packages_month3',
            new_name='enn_packages_month3',
        ),
        migrations.RenameField(
            model_name='t_national_shipment',
            old_name='een_packages_month4',
            new_name='enn_packages_month4',
        ),
        migrations.RenameField(
            model_name='t_national_shipment',
            old_name='een_packages_month5',
            new_name='enn_packages_month5',
        ),
        migrations.RenameField(
            model_name='t_national_shipment',
            old_name='een_packages_month6',
            new_name='enn_packages_month6',
        ),
    ]
