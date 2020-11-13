from django.contrib import admin
from .models import *
from django.utils.html import format_html

class CakeAdmin(admin.ModelAdmin):
    list_filter = ('category', )
    class Meta:
        model = Cake

class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category

class MarsipanAdmin(admin.ModelAdmin):
    list_filter = ('category', )
    class Meta:
        model = Marsipan

class MarsipanCategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = MarsipanCategory

class FlowerAdmin(admin.ModelAdmin):
    list_filter = ('category', )
    class Meta:
        model = Flower

class FlowerCategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = FlowerCategory

class XoncaAdmin(admin.ModelAdmin):
    list_filter = ('category', )
    class Meta:
        model = Xonca

class XoncaCategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = XoncaCategory


class CafeAdmin(admin.ModelAdmin):
    list_display = ('image_tag', )
    def image_tag(self,obj):
        return format_html('<img src="{0}" style="width: autopx; height:100px;" />'.format(obj.image.url))
    class Meta:
        model = Cafe

class ContactAdmin(admin.ModelAdmin):
    class Meta:
        model = Contact

admin.site.register(Cake, CakeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Marsipan, MarsipanAdmin)
admin.site.register(MarsipanCategory, MarsipanCategoryAdmin)
admin.site.register(Flower, FlowerAdmin)
admin.site.register(FlowerCategory, FlowerCategoryAdmin)
admin.site.register(Xonca, XoncaAdmin)
admin.site.register(XoncaCategory, XoncaCategoryAdmin)
admin.site.register(Cafe, CafeAdmin)
admin.site.register(Contact, ContactAdmin)