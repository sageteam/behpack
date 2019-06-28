from django.contrib import admin


from .models import AwardsContent
from .models import WebsiteContent

# Register your models here.

@admin.register(AwardsContent)
class AwardsContentAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku',)


@admin.register(WebsiteContent)
class WebsiteContentAdmin(admin.ModelAdmin):
    list_display = ('quality1', 'quality2', 'quality3')


