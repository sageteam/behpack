from django.db import models

import secrets
from painless import functions as func

###########################
#####    WEBSITE      #####
###########################

# Create your models here.
class SlovakiWebsiteContent(models.Model):
    about = models.TextField()

    # Advertisement
    title1 = models.CharField(max_length = 16)
    title2 = models.CharField(max_length = 16)
    description1 = models.TextField()
    description2 = models.TextField()

    # Feature
    quality1 = models.CharField(max_length = 128)
    quality2 = models.CharField(max_length = 128)
    quality3 = models.CharField(max_length = 128)
    summary_feature = models.TextField()
    description_feature = models.TextField()

    def __str__(self):
        return 'website content'


class SlovakiAwardsContent(models.Model):
    sku = models.CharField(max_length = 15, default = secrets.token_urlsafe(8), help_text = 'Unique code for refrence to supervisors' )
    name = models.CharField(max_length = 128)
    pic = models.ImageField(upload_to = func.upload_location, null = True, blank = True)
    submit_date = models.DateTimeField(null = True)


##############################
#######      NEWS      #######
##############################
class SlovakiNewsTags(models.Model):
    tag_name = models.CharField(max_length = 128)


    def __str__(self):
        return self.tag_name

    class Meta:
        ordering = ('tag_name',)
        verbose_name = 'News Tag'
        verbose_name_plural = 'News Tags'


class SlovakiNewsPhotos(models.Model):
    sku = models.CharField(max_length = 15, default = secrets.token_urlsafe(8), help_text = 'Unique code for refrence to supervisors' )
    photo_name = models.CharField(max_length = 128)
    pic = models.ImageField(upload_to = func.upload_location, null = True, blank = True)

    def __str__(self):
        return self.photo_name
    
    
    class Meta:
        verbose_name = 'News Photo'
        verbose_name_plural = 'News Photos'


class SlovakiNewsMovies(models.Model):
    sku = models.CharField(max_length = 15, default = secrets.token_urlsafe(8), help_text = 'Unique code for refrence to supervisors' )
    movie_name = models.CharField(max_length = 128)
    movie = models.FileField(upload_to=func.upload_location, null = True, blank = True)

    def __str__(self):
        return self.movie_name


    class Meta:
        verbose_name = 'News Movie'
        verbose_name_plural = 'News Movies'


class SlovakiNewsGroup(models.Model):
    group_name = models.CharField(max_length = 128)

    def __str__(self):
        return self.group_name


    class Meta:
        verbose_name = 'News Group'
        verbose_name_plural = 'News Groups'


class SlovakiNews(models.Model):
    sku = models.CharField(max_length = 15, default = secrets.token_urlsafe(8), help_text = 'Unique code for refrence to supervisors' )
    title = models.CharField(max_length = 128)
    summary = models.CharField(max_length = 2048)
    description = models.TextField()
    tags = models.ManyToManyField(SlovakiNewsTags)
    photos = models.ManyToManyField(SlovakiNewsPhotos)
    movies = models.ManyToManyField(SlovakiNewsMovies)
    groups = models.ManyToManyField(SlovakiNewsGroup)
    submit_date = models.DateTimeField(auto_now_add = True)

    verbose_name = 'News'
    verbose_name_plural = 'News'

    def __str__(self):
        return self.title
    

    class Meta:
        ordering = ('-submit_date', 'title',)
        verbose_name = 'News'
        verbose_name_plural = 'News'


#############################
#######    Product      #####
#############################
class SlovakiProductTags(models.Model):
    tag_name = models.CharField(max_length = 128)


    def __str__(self):
        return self.tag_name

    class Meta:
        ordering = ('tag_name',)
        verbose_name = 'Product Tag'
        verbose_name_plural = 'Product Tags'


class SlovakiProductPhotos(models.Model):
    sku = models.CharField(max_length = 15, default = secrets.token_urlsafe(8), help_text = 'Unique code for refrence to supervisors' )
    photo_name = models.CharField(max_length = 128)
    pic = models.ImageField(upload_to = func.upload_location, null = True, blank = True)

    def __str__(self):
        return self.photo_name
    
    
    class Meta:
        verbose_name = 'Product Photo'
        verbose_name_plural = 'Product Photos'


class SlovakiProductMovies(models.Model):
    sku = models.CharField(max_length = 15, default = secrets.token_urlsafe(8), help_text = 'Unique code for refrence to supervisors' )
    movie_name = models.CharField(max_length = 128)
    movie = models.FileField(upload_to=func.upload_location, null = True, blank = True)

    def __str__(self):
        return self.movie_name


    class Meta:
        verbose_name = 'Product Movie'
        verbose_name_plural = 'Product Movies'


class SlovakiProductGroup(models.Model):
    group_name = models.CharField(max_length = 128)

    def __str__(self):
        return self.group_name


    class Meta:
        verbose_name = 'Product Group'
        verbose_name_plural = 'Product Groups'


class SlovakiProduct(models.Model):
    sku = models.CharField(max_length = 15, default = secrets.token_urlsafe(8), help_text = 'Unique code for refrence to supervisors' )
    title = models.CharField(max_length = 128)
    summary = models.CharField(max_length = 2048, help_text = 'Max Length of this field is 2048 characters.')
    description = models.TextField()
    tags = models.ManyToManyField(SlovakiProductTags)
    photos = models.ManyToManyField(SlovakiProductPhotos)
    movies = models.ManyToManyField(SlovakiProductMovies)
    groups = models.ManyToManyField(SlovakiProductGroup)
    submit_date = models.DateTimeField(auto_now_add = True)

    verbose_name = 'Product'
    verbose_name_plural = 'Product'

    def __str__(self):
        return self.title
    

    class Meta:
        ordering = ('-submit_date', 'title',)
        verbose_name = 'Product'
        verbose_name_plural = 'Product'
