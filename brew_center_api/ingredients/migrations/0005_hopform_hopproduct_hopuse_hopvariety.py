# Generated by Django 3.2.7 on 2021-10-27 14:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0004_auto_20211027_1410'),
    ]

    operations = [
        migrations.CreateModel(
            name='HopForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='HopUse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='HopVariety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('notes', models.TextField(blank=True, null=True)),
                ('substitutes', models.ManyToManyField(related_name='_ingredients_hopvariety_substitutes_+', to='ingredients.HopVariety')),
                ('uses', models.ManyToManyField(related_name='varieties', to='ingredients.HopUse')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='HopProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(blank=True, max_length=255, null=True)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(2050)])),
                ('alpha_acid_percent', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('beta_acid_percent', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('total_oil_mk_per_100g', models.FloatField(blank=True, null=True)),
                ('humulene_percent', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('caryophyllene_percent', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('myrcene_percent', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('farnesene_percent', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('geraniol_percent', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('b_pinene_percent', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('linalool_percent', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('limonene_percent', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('nerol_percent', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('pinene_percent', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('polyphenols_percent', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('xanthohumol_percent', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='ingredients.hopform')),
                ('manufacturer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ingredients.manufacturer')),
                ('origin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ingredients.origin')),
                ('variety', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='ingredients.hopvariety')),
            ],
            options={
                'order_with_respect_to': 'variety',
            },
        ),
    ]
