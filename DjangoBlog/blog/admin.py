from django.contrib import admin
from .models import Tag, Category, Article

# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'         #后台管理表单Article可以按照创建时间分组展示
    list_display = ('title', 'category', 'author', 'created_date', 'view')  #设置后台管理表单Article的字段
    list_filter = ('category', 'author')    #设置台管理表单Article过滤器
    filter_horizontal = ('tag',)            #创建文章的时候，tag以水平迁移框的形式表现