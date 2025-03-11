from django.contrib import admin

from django.utils import timezone
timezone.activate("Asia/Bangkok")

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','barcode',  'price','stock',
                  'updated_at','updated_by' )
    search_fields = ['name', 'barcode']
    list_per_page = 20
    readonly_fields = ['updated_by']
    actions = ['delete_selected']

    class Media:
        js = ('js/custom_admin.js',)

    def save_model(self, request, obj, form, change):
        # Set the user field with the currently logged-in user


        if not obj.updated_by:
            obj.updated_by = request.user
        obj.save()
    




# Register your models here.
admin.site.register(Product, ProductAdmin)

admin.site.site_header  =  "Product Tracking Book"
