# Generated by Django 2.0.6 on 2018-06-05 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180605_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='sku',
            field=models.CharField(default='3nH8ipceSho', help_text='Unique code for refrence to supervisors', max_length=15),
        ),
        migrations.AlterField(
            model_name='newsmovies',
            name='sku',
            field=models.CharField(default='RFlIaEirS50', help_text='Unique code for refrence to supervisors', max_length=15),
        ),
        migrations.AlterField(
            model_name='newsphotos',
            name='sku',
            field=models.CharField(default='clO4CaHAd80', help_text='Unique code for refrence to supervisors', max_length=15),
        ),
    ]