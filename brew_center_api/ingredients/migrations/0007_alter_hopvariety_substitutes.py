# Generated by Django 3.2.7 on 2021-10-27 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0006_auto_20211027_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hopvariety',
            name='substitutes',
            field=models.ManyToManyField(blank=True, null=True, related_name='_ingredients_hopvariety_substitutes_+', to='ingredients.HopVariety'),
        ),
    ]