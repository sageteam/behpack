# Generated by Django 2.0.6 on 2018-06-05 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20180605_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awardscontent',
            name='sku',
            field=models.CharField(default='U3S-uBZlLKw', help_text='Unique code for refrence to supervisors', max_length=15),
        ),
    ]
