from django.db import models

import secrets

from accounts.models import User
from painless import functions as func


##############################
#######      Product      #######
##############################
class ProductTags(models.Model):
    tag_name = models.CharField(max_length = 128)


    def __str__(self):
        return self.tag_name

    class Meta:
        ordering = ('tag_name',)
        verbose_name = 'Product Tag'
        verbose_name_plural = 'Product Tags'


class ProductPhotos(models.Model):
    sku = models.CharField(max_length = 15, editable=False, default = secrets.token_urlsafe(8), help_text = 'Unique code for refrence to supervisors')
    photo_name = models.CharField(max_length = 128)
    pic = models.ImageField(upload_to = func.upload_location, null = True, blank = True)

    def __str__(self):
        return self.photo_name
    
    
    class Meta:
        verbose_name = 'Product Photo'
        verbose_name_plural = 'Product Photos'


class ProductMovies(models.Model):
    sku = models.CharField(max_length = 15, editable=False, default = secrets.token_urlsafe(8), help_text = 'Unique code for refrence to supervisors' )
    movie_name = models.CharField(max_length = 128)
    movie = models.FileField(upload_to=func.upload_movie_location, null = True, blank = True)

    def __str__(self):
        return self.movie_name


    class Meta:
        verbose_name = 'Product Movie'
        verbose_name_plural = 'Product Movies'


class ProductGroup(models.Model):
    group_name = models.CharField(max_length = 128)

    def __str__(self):
        return self.group_name


    class Meta:
        verbose_name = 'Product Group'
        verbose_name_plural = 'Product Groups'


class Product(models.Model):
    sku = models.CharField(max_length = 15, editable=False, default = secrets.token_urlsafe(8), help_text = 'Unique code for refrence to supervisors' )
    title = models.CharField(max_length = 128)
    summary = models.CharField(max_length = 2048, help_text = 'Max Length of this field is 2048 characters.')
    description = models.TextField()
    tags = models.ManyToManyField(ProductTags)
    photos = models.ManyToManyField(ProductPhotos)
    movies = models.ManyToManyField(ProductMovies)
    groups = models.ManyToManyField(ProductGroup)
    submit_date = models.DateTimeField(auto_now_add = True)

    verbose_name = 'Product'
    verbose_name_plural = 'Product'

    def __str__(self):
        return self.title
    

    class Meta:
        ordering = ('-submit_date', 'title',)
        verbose_name = 'Product'
        verbose_name_plural = 'Product'
