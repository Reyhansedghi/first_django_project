from django.contrib import admin
from .models import Product,ProductsCategory,ProductsSubCategory,ProductsSubSubCategory
# Register your models here.
admin.site.register(ProductsCategory)
admin.site.register(ProductsSubCategory)
admin.site.register(ProductsSubSubCategory)

@admin.register(Product)
class Goods_Admin(admin.ModelAdmin):
    list_display=('is_seller','is_legal','user','grade','certificate',
                  'get_category','get_subcategory','get_subsubcategory',
                  'title','thumbnail','slug','consumed','performance','constituents',
                  'analytical_material','description','color','count',
                  'capacity','purchaseprice','sellingprice','manufacturers',)
    list_filter=('user','is_seller','is_legal',)
    search_fields=('user','title','description',)
    prepopulated_fields={'slug':('title',)}


