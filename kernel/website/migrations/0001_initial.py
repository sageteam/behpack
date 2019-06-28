# Generated by Django 2.0.6 on 2018-06-05 09:23

from django.db import migrations, models
import painless.functions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AwardsContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(default='Y8bseSazzQY', help_text='Unique code for refrence to supervisors', max_length=15)),
                ('name', models.CharField(max_length=128)),
                ('pic', models.ImageField(blank=True, null=True, upload_to=painless.functions.upload_location)),
            ],
        ),
        migrations.CreateModel(
            name='WebsiteContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField()),
                ('title1', models.CharField(max_length=16)),
                ('title2', models.CharField(max_length=16)),
                ('description1', models.TextField()),
                ('description2', models.TextField()),
                ('quality1', models.CharField(max_length=128)),
                ('quality2', models.CharField(max_length=128)),
                ('quality3', models.CharField(max_length=128)),
                ('summary_feature', models.TextField()),
                ('description_feature', models.TextField()),
            ],
        ),
    ]
