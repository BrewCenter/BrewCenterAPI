# Generated by Django 3.2.7 on 2021-10-27 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0007_alter_hopvariety_substitutes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fermentablebase',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
