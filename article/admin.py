from django.contrib import admin
from article.models import Article, Category, Tag


class ArticleAdmin (admin.ModelAdmin):

    list_display = ['title', 'create_time', 'category']

# Register your models here.
admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)