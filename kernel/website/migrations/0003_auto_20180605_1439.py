# Generated by Django 2.0.6 on 2018-06-05 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20180605_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awardscontent',
            name='sku',
            field=models.CharField(default='wACzyn3BER8', help_text='Unique code for refrence to supervisors', max_length=15),
        ),
    ]
