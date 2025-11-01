from django.contrib import admin
from website.models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display=['name','subject','email','created_date','updated_date']
    list_filter=['name','email']
    date_hierarchy='created_date'
    search_fields=['name','message']
    ordering=['created_date']



admin.site.register(Contact,ContactAdmin)