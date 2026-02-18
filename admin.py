from django.contrib import admin
from .models import *
# Register your models here.

class contactusAdmin(admin.ModelAdmin):
    list_display = ('id','Name','Email','Mobile','Message')

admin.site.register(contactus,contactusAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display=('id','category_name','category_picture')
admin.site.register(category,categoryAdmin)

class tbl_jobsAdmin(admin.ModelAdmin):
    list_display=('id','title_link','post_date')
admin.site.register(tbl_jobs,tbl_jobsAdmin)

class tbl_sliderAdmin(admin.ModelAdmin):
    list_display=('id','picture','title','description')
admin.site.register(tbl_slider,tbl_sliderAdmin)

class tbl_cityAdmin(admin.ModelAdmin):
    list_display=('id','city_name','city_picture')
admin.site.register(tbl_city,tbl_cityAdmin)

class tbl_newsAdmin(admin.ModelAdmin):
    list_display=('id','headline','news_category','news_description','posted_date','news_picture')
admin.site.register(tbl_news,tbl_newsAdmin)

class video_newsAdmin(admin.ModelAdmin):
    list_display=('id','news_headline','news_description','video_link','posted_date')
admin.site.register(video_news,video_newsAdmin)