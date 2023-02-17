from django.contrib import admin

# Register your models here.



from .models import Jewellery,Fashion,Electronic



class jewelleryAdmin(admin.ModelAdmin):
    list_display=['id','name','price']
    list_filter=['price']
    list_editable=['name','price']
    search_fields=['name','price']


class fashionAdmin(admin.ModelAdmin):
    list_display=['id','name','price']
    list_filter=['price']
    list_editable=['name','price']
    search_fields=['name','price']


class electronicAdmin(admin.ModelAdmin):
    list_display=['id','name','price']
    list_filter=['price']
    list_editable=['name','price']
    search_fields=['name','price']

admin.site.register(Jewellery,jewelleryAdmin)
admin.site.register(Fashion,fashionAdmin)
admin.site.register(Electronic,electronicAdmin)