from django.contrib import admin
from .models import *

#聲明高級管理類
class AuthorAdmin(admin.ModelAdmin):
  list_display = ('name','age','email')
  list_display_links = ('name','email')
  list_editable = ('age',)
  search_fields = ('name','email')
  list_filter=('name',)
  fieldsets = (
    #分組1
    ('基本信息',{
      'fields':('name','email'),
    }),
    #分組2
    ('可選信息',{
      'fields':('age','isActive','picture'),
      'classes':('collapse',),
    })
  )


class BookAdmin(admin.ModelAdmin):
  date_hierarchy = "publicate_date"


class PublisherAdmin(admin.ModelAdmin):
  list_display = ('name','address','city','website')
  list_editable = ('address','city')
  list_filter = ('address','city')
  search_fields = ('name','website')
  fieldsets = (
    ('基本選項',{
      'fields':('name','address','city'),
    }),
    (
      '高級選項',{
        'fields':('country','website'),
        'classes':('collapse',)
      }
    )
  )


# Register your models here.
admin.site.register(Author,AuthorAdmin)
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Wife)
