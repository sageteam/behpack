# Generated by Django 2.0.6 on 2018-06-05 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20180605_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(default='GNJwyr6Eo-U', help_text='Unique code for refrence to supervisors', max_length=15),
        ),
        migrations.AlterField(
            model_name='productmovies',
            name='sku',
            field=models.CharField(default='7P1qLd3z7t8', help_text='Unique code for refrence to supervisors', max_length=15),
        ),
        migrations.AlterField(
            model_name='productphotos',
            name='sku',
            field=models.CharField(default='R09Hzqrra4Q', help_text='Unique code for refrence to supervisors', max_length=15),
        ),
    ]
