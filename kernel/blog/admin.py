from django.contrib import admin

from .models import News
from .models import NewsGroup
from .models import NewsMovies
from .models import NewsPhotos
from .models import NewsTags


##############################
#######      NEWS      #######
##############################

@admin.register(NewsGroup)
class NewsGroupAdmin(admin.ModelAdmin):
    list_display = ('group_name',)


@admin.register(NewsTags)
class NewsTags(admin.ModelAdmin):
    list_display = ('tag_name',)


@admin.register(NewsPhotos)
class NewsPhotos(admin.ModelAdmin):
    list_display = ('photo_name',)


@admin.register(NewsMovies)
class NewsMovies(admin.ModelAdmin):
    list_display = ('movie_name',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_tags', 'get_groups', 'submit_date')
    list_filter = ('tags', 'groups', 'submit_date', )
    search_fields = ('title', 'summary', 'sku')
    empty_value_display = '-empty-'    

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(NewsAdmin, self).get_inline_instances(request, obj)
    

    def get_tags(self, instance):
        return ", ".join([t.tag_name for t in instance.tags.all()])


    def get_groups(self, instance):
        return ", ".join([g.group_name for g in instance.groups.all()])

    get_tags.short_description = 'tags'
    get_groups.short_description = 'groups'
    
