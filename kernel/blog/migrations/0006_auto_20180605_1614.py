# Generated by Django 2.0.6 on 2018-06-05 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180605_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='sku',
            field=models.CharField(default='Rd-mFN6iFB4', help_text='Unique code for refrence to supervisors', max_length=15),
        ),
        migrations.AlterField(
            model_name='newsmovies',
            name='sku',
            field=models.CharField(default='PoQh7C2U0Gs', help_text='Unique code for refrence to supervisors', max_length=15),
        ),
        migrations.AlterField(
            model_name='newsphotos',
            name='sku',
            field=models.CharField(default='yJ86bBxpkG4', help_text='Unique code for refrence to supervisors', max_length=15),
        ),
    ]
