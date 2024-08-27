from django.contrib import admin
from .models import Post,Comment


admin.site.register(Post)




@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display=('user','percentage','title','pos','neg','body','thumbnail','created_on','active',)
    
    list_filter=('user','title','active','percentage',)
    search_fields=('user','title','body')
    actions=['approve_comments']
    def approve_comments(self,request,queryset):
        queryset.update(active=True)