from django.contrib import admin
from article.models import Article, Comments

# Register your models here.

class ArticleInLine(admin.StackedInline):
    """устанавливает отображении комментариев под статьями в административной панели"""
    model = Comments
    #extra = 5

class ArticleAdmin(admin.ModelAdmin):
    """устанавливает какие поля будут видны в административной панели"""
    fields = ['article_title', 'article_text', 'article_date']
    inlines = [ArticleInLine] #показывает, то будет отображено снизу под нашими полями
    list_filter = ['article_date'] #show filter into Django admin`s panel

admin.site.register(Article, ArticleAdmin)
