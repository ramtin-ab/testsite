from django.contrib import admin
from blog.models import *
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    #fields exclude baraye form hast yani safhe khode post yani yek chizaei dar model hast nemikhaym dar dakhel admin dar safhe marbot be khode model onja ke moshakhasat post vared mikoni neshon bede
    list_display=['title','status','author','published_date','counted_view','created_date']
    date_hierarchy='published_date'
    empty_value_display='-empty-'
    search_fields=['title','content']
    list_filter=['status','author']
    ordering=['created_date']
    

admin.site.register(Post,PostAdmin)
admin.site.register(Category)