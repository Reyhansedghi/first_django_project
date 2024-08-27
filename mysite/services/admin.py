from django.contrib import admin
from .models import Services,ServicesCategory,ServicesSubCategory,ServicesSubSubCategory
# Register your models here.
admin.site.register(ServicesCategory)
admin.site.register(ServicesSubCategory)
admin.site.register(ServicesSubSubCategory)
# Register your models here.


@admin.register(Services)
class Services_Admin(admin.ModelAdmin):
    list_display=('slug','user','title','description','get_category','get_subcategory','get_subsubcategory','grade','certificate','is_legal','is_seller',)
    
    list_filter=('user','is_seller','is_legal',)
    search_fields=('user','title','body')
    prepopulated_fields={'slug':('title',)}

