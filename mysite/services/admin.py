from django.contrib import admin
from .models import Services,ServicesCategory
# Register your models here.

admin.site.register(ServicesCategory)

   


@admin.register(Services)
class Services_Admin(admin.ModelAdmin):
    list_display=('userstatus','user','get_category','title','slug','description','capacity','price',)
    
    list_filter=('user','userstatus',)
    search_fields=('user','title','body')
    prepopulated_fields={'slug':('title',)}

