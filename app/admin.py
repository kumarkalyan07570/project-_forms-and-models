from django.contrib import admin

# Register your models here.

from app.models import *




class customizeWeb(admin.ModelAdmin):
    #list_display=['data_name','web_name','web_subject','web_data']
    #list_display_Links=['web_name']
    #list_Editable=['web_name','kalyan']
    #search_fields=['web_name']
    #list_filter('Web_name',)
    list_per_page=1

admin.site .register(Data)

admin.site.register(Web,customizeWeb)


