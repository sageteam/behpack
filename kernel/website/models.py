from django.db import models
from painless import functions as func
import secrets

# Create your models here.
class WebsiteContent(models.Model):
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


class AwardsContent(models.Model):
    sku = models.CharField(max_length = 15, default = secrets.token_urlsafe(8), help_text = 'Unique code for refrence to supervisors' )
    name = models.CharField(max_length = 128)
    pic = models.ImageField(upload_to = func.upload_location, null = True, blank = True)
    submit_date = models.DateTimeField(null = True)

