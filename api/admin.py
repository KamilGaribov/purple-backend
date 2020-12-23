from django.contrib import admin
from .models import *
from django.utils.html import format_html

class VitrinAdmin(admin.ModelAdmin):
    list_filter = ('category', )
    class Meta:
        model = Vitrin

class VitrinCategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = VitrinCategory

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

class HomePageProductAdmin(admin.ModelAdmin):
    class Meta:
        model = HomePageProduct

class OrderProductAdmin(admin.TabularInline):
    # model = OrderProduct
    fields = ('quantity', 'url_display', )
    readonly_fields = ('quantity', 'url_display')

    def url_display(self, obj):
        if obj.product:
            return format_html(f'<a href={obj.url}>{obj.product}</a>')
        return ''
    # def url_tag(self, obj):
    #     return 'salam'
    # url_tag.allow_tags = True
    # def get_readonly_fields(self, request, obj=None):
    #     return [f.name for f in self.model._meta.fields]
    # class Meta:
    model = OrderProduct

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderProductAdmin, ]
    search_fields = ('name', )
    list_filter = ('status', )
    # readonly_fields = ('sessionid', 'orderid', 'pan', 'amount', 'created_at', 'status', )
    # readonly_fields = '__all__'
    def get_readonly_fields(self, request, obj=None):
        return [f.name for f in self.model._meta.fields]

    # actions = ['make_tags_active']
    # def make_tags_active(self, request, queryset):
    #     queryset.update(status='approved')
    # make_tags_active.short_description = "Mark selected tags as active"
    class Meta:
        model = Order

admin.site.register(Vitrin, VitrinAdmin)
admin.site.register(VitrinCategory, VitrinCategoryAdmin)
admin.site.register(Marsipan, MarsipanAdmin)
admin.site.register(MarsipanCategory, MarsipanCategoryAdmin)
admin.site.register(Flower, FlowerAdmin)
admin.site.register(FlowerCategory, FlowerCategoryAdmin)
admin.site.register(Xonca, XoncaAdmin)
admin.site.register(XoncaCategory, XoncaCategoryAdmin)
admin.site.register(Cafe, CafeAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(HomePageProduct, HomePageProductAdmin)
admin.site.register(Order, OrderAdmin)


# admin.site.register(OrderProduct, OrderProductAdmin)