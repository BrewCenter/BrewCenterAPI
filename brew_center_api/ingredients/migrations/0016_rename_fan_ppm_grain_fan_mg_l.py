# Generated by Django 4.1.7 on 2023-02-27 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0015_remove_origin_country_origin_country_code_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grain',
            old_name='fan_ppm',
            new_name='fan_mg_l',
        ),
    ]
