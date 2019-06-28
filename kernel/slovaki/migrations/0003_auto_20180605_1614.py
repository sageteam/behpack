# Generated by Django 2.0.6 on 2018-06-05 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slovaki', '0002_auto_20180605_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='slovakiawardscontent',
            name='submit_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='slovakiawardscontent',
            name='sku',
            field=models.CharField(default='cDyMeobnd9Q', help_text='Unique code for refrence to supervisors', max_length=15),
        ),
        migrations.AlterField(
            model_name='slovakinews',
            name='sku',
            field=models.CharField(default='97pR-pi2aro', help_text='Unique code for refrence to supervisors', max_length=15),
        ),
        migrations.AlterField(
            model_name='slovakinewsmovies',
            name='sku',
            field=models.CharField(default='O4boPgHE5Dg', help_text='Unique code for refrence to supervisors', max_length=15),
        ),
        migrations.AlterField(
            model_name='slovakinewsphotos',
            name='sku',
            field=models.CharField(default='Yzl5XyQ2w-c', help_text='Unique code for refrence to supervisors', max_length=15),
        ),
        migrations.AlterField(
            model_name='slovakiproduct',
            name='sku',
            field=models.CharField(default='Cc_9BGrzJ4U', help_text='Unique code for refrence to supervisors', max_length=15),
        ),
        migrations.AlterField(
            model_name='slovakiproductmovies',
            name='sku',
            field=models.CharField(default='_jXUmE_hcRA', help_text='Unique code for refrence to supervisors', max_length=15),
        ),
        migrations.AlterField(
            model_name='slovakiproductphotos',
            name='sku',
            field=models.CharField(default='O5NW4mIt58k', help_text='Unique code for refrence to supervisors', max_length=15),
        ),
    ]