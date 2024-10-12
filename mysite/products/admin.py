from django.contrib import admin
from .models import Product,ProductsCategory
# Register your models here.

admin.site.register(ProductsCategory)



@admin.register(Product)
class Goods_Admin(admin.ModelAdmin):
    list_display=('userstatus','user',
                  'get_category',
                  'title','thumbnail','slug','consumed','constituents',
                  'analytical_material','description','color','count',
                  'capacity','price','manufacturers',)
    list_filter=('user','userstatus',)
    search_fields=('user','title','description',)
    prepopulated_fields={'slug':('title',)}


