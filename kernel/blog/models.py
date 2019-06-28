from django.db import models

import secrets

from accounts.models import User
from painless import functions as func


##############################
#######      NEWS      #######
##############################
class NewsTags(models.Model):
    tag_name = models.CharField(max_length = 128)


    def __str__(self):
        return self.tag_name

    class Meta:
        ordering = ('tag_name',)
        verbose_name = 'News Tag'
        verbose_name_plural = 'News Tags'


class NewsPhotos(models.Model):
    sku = models.CharField(max_length = 15, default = secrets.token_urlsafe(8), help_text = 'Unique code for refrence to supervisors' )
    photo_name = models.CharField(max_length = 128)
    pic = models.ImageField(upload_to = func.upload_location, null = True, blank = True)

    def __str__(self):
        return self.photo_name
    
    
    class Meta:
        verbose_name = 'News Photo'
        verbose_name_plural = 'News Photos'


class NewsMovies(models.Model):
    sku = models.CharField(max_length = 15, default = secrets.token_urlsafe(8), help_text = 'Unique code for refrence to supervisors' )
    movie_name = models.CharField(max_length = 128)
    movie = models.FileField(upload_to=func.upload_location, null = True, blank = True)

    def __str__(self):
        return self.movie_name


    class Meta:
        verbose_name = 'News Movie'
        verbose_name_plural = 'News Movies'


class NewsGroup(models.Model):
    group_name = models.CharField(max_length = 128)

    def __str__(self):
        return self.group_name


    class Meta:
        verbose_name = 'News Group'
        verbose_name_plural = 'News Groups'


class News(models.Model):
    sku = models.CharField(max_length = 15, default = secrets.token_urlsafe(8), help_text = 'Unique code for refrence to supervisors' )
    title = models.CharField(max_length = 128)
    summary = models.CharField(max_length = 2048)
    description = models.TextField()
    tags = models.ManyToManyField(NewsTags)
    photos = models.ManyToManyField(NewsPhotos)
    movies = models.ManyToManyField(NewsMovies)
    groups = models.ManyToManyField(NewsGroup)
    submit_date = models.DateTimeField(auto_now_add = True)

    verbose_name = 'News'
    verbose_name_plural = 'News'

    def __str__(self):
        return self.title
    

    class Meta:
        ordering = ('-submit_date', 'title',)
        verbose_name = 'News'
        verbose_name_plural = 'News'
