from django.contrib import admin

from .models import SlovakiAwardsContent
from .models import SlovakiNews
from .models import SlovakiNewsGroup
from .models import SlovakiNewsMovies
from .models import SlovakiNewsPhotos
from .models import SlovakiNewsTags
from .models import SlovakiProduct
from .models import SlovakiProductGroup
from .models import SlovakiProductMovies
from .models import SlovakiProductPhotos
from .models import SlovakiProductTags
from .models import SlovakiWebsiteContent




##############################
#######      NEWS      #######
##############################

@admin.register(SlovakiNewsGroup)
class SlovakiNewsGroupAdmin(admin.ModelAdmin):
    list_display = ('group_name',)


@admin.register(SlovakiNewsTags)
class SlovakiNewsTags(admin.ModelAdmin):
    list_display = ('tag_name',)


@admin.register(SlovakiNewsPhotos)
class SlovakiNewsPhotos(admin.ModelAdmin):
    list_display = ('photo_name',)


@admin.register(SlovakiNewsMovies)
class SlovakiNewsMovies(admin.ModelAdmin):
    list_display = ('movie_name',)


@admin.register(SlovakiNews)
class SlovakiNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_tags', 'get_groups', 'submit_date')
    list_filter = ('tags', 'groups', 'submit_date', )
    search_fields = ('title', 'summary', 'sku')
    empty_value_display = '-empty-'    

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(SlovakiNewsAdmin, self).get_inline_instances(request, obj)
    

    def get_tags(self, instance):
        return ", ".join([t.tag_name for t in instance.tags.all()])


    def get_groups(self, instance):
        return ", ".join([g.group_name for g in instance.groups.all()])

    get_tags.short_description = 'tags'
    get_groups.short_description = 'groups'
    



#############################
#######    Product      #####
#############################

@admin.register(SlovakiProductGroup)
class SlovakiProductGroupAdmin(admin.ModelAdmin):
    list_display = ('group_name',)


@admin.register(SlovakiProductTags)
class SlovakiProductTags(admin.ModelAdmin):
    list_display = ('tag_name',)


@admin.register(SlovakiProductPhotos)
class SlovakiProductPhotos(admin.ModelAdmin):
    list_display = ('photo_name',)


@admin.register(SlovakiProductMovies)
class SlovakiProductMovies(admin.ModelAdmin):
    list_display = ('movie_name',)


@admin.register(SlovakiProduct)
class SlovakiProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_tags', 'get_groups', 'submit_date')
    list_filter = ('tags', 'groups', 'submit_date', )
    search_fields = ('title', 'summary', 'sku')
    empty_value_display = '-empty-'    

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(SlovakiProductAdmin, self).get_inline_instances(request, obj)
    

    def get_tags(self, instance):
        return ", ".join([t.tag_name for t in instance.tags.all()])


    def get_groups(self, instance):
        return ", ".join([g.group_name for g in instance.groups.all()])

    get_tags.short_description = 'tags'
    get_groups.short_description = 'groups'


#############################
#######    WEBSITE      #####
#############################

@admin.register(SlovakiAwardsContent)
class SlovakiAwardsContentAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku',)


@admin.register(SlovakiWebsiteContent)
class SlovakiWebsiteContentAdmin(admin.ModelAdmin):
    list_display = ('quality1', 'quality2', 'quality3')

