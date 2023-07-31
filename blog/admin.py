from django.contrib import admin
from blog.models import Post,Category,Comment
# Register your models here.



class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title' ,'author','status','login_require','created_date','published_date')
    list_filter = ('status',)
    search_fields = ['title','content']

class PostComment(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name' ,'post','created_date','approach')
    list_filter = ('post','approach',)
    search_fields = ['name','post']
    
admin.site.register(Category)
admin.site.register(Comment,PostComment)
admin.site.register(Post,PostAdmin)
