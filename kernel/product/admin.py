from django.contrib import admin

from .models import Product
from .models import ProductGroup
from .models import ProductMovies
from .models import ProductPhotos
from .models import ProductTags


##############################
#######    PRODUCTS    #######
##############################

@admin.register(ProductGroup)
class ProductGroupAdmin(admin.ModelAdmin):
    list_display = ('group_name',)


@admin.register(ProductTags)
class ProductTags(admin.ModelAdmin):
    list_display = ('tag_name',)


@admin.register(ProductPhotos)
class ProductPhotos(admin.ModelAdmin):
    list_display = ('photo_name',)


@admin.register(ProductMovies)
class ProductMovies(admin.ModelAdmin):
    list_display = ('movie_name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_tags', 'get_groups', 'submit_date')
    list_filter = ('tags', 'groups', 'submit_date', )
    search_fields = ('title', 'summary', 'sku')
    empty_value_display = '-empty-'    

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(ProductAdmin, self).get_inline_instances(request, obj)
    

    def get_tags(self, instance):
        return ", ".join([t.tag_name for t in instance.tags.all()])


    def get_groups(self, instance):
        return ", ".join([g.group_name for g in instance.groups.all()])

    get_tags.short_description = 'tags'
    get_groups.short_description = 'groups'
    
