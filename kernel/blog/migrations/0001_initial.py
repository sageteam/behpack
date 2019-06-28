# Generated by Django 2.0.6 on 2018-06-05 05:45

from django.db import migrations, models
import painless.functions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(default='erDs0Ux3lcg', help_text='Unique code for refrence to supervisors', max_length=15)),
                ('title', models.CharField(max_length=128)),
                ('summary', models.CharField(max_length=2048)),
                ('description', models.TextField()),
                ('submit_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
                'ordering': ('-submit_date', 'title'),
            },
        ),
        migrations.CreateModel(
            name='NewsGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'News Group',
                'verbose_name_plural': 'News Groups',
            },
        ),
        migrations.CreateModel(
            name='NewsMovies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(default='URw2xZc-gh0', help_text='Unique code for refrence to supervisors', max_length=15)),
                ('movie_name', models.CharField(max_length=128)),
                ('movie', models.FileField(blank=True, null=True, upload_to=painless.functions.upload_location)),
            ],
            options={
                'verbose_name': 'News Movie',
                'verbose_name_plural': 'News Movies',
            },
        ),
        migrations.CreateModel(
            name='NewsPhotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(default='hd6ZOTcOts0', help_text='Unique code for refrence to supervisors', max_length=15)),
                ('photo_name', models.CharField(max_length=128)),
                ('pic', models.ImageField(blank=True, null=True, upload_to=painless.functions.upload_location)),
            ],
            options={
                'verbose_name': 'News Photo',
                'verbose_name_plural': 'News Photos',
            },
        ),
        migrations.CreateModel(
            name='NewsTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'News Tag',
                'verbose_name_plural': 'News Tags',
                'ordering': ('tag_name',),
            },
        ),
        migrations.AddField(
            model_name='news',
            name='groups',
            field=models.ManyToManyField(to='blog.NewsGroup'),
        ),
        migrations.AddField(
            model_name='news',
            name='movies',
            field=models.ManyToManyField(to='blog.NewsMovies'),
        ),
        migrations.AddField(
            model_name='news',
            name='photos',
            field=models.ManyToManyField(to='blog.NewsPhotos'),
        ),
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(to='blog.NewsTags'),
        ),
    ]