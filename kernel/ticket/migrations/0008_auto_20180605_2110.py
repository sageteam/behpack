# Generated by Django 2.0.6 on 2018-06-05 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0007_auto_20180605_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='sku',
            field=models.CharField(default='pzJNj3txbi0', help_text='Unique code for refrence to supervisors', max_length=15),
        ),
    ]
