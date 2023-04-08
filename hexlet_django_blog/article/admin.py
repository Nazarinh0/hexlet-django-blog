from django.contrib import admin
from .models import Article
# Register your models here.


@admin.register(Article)  # equals to commented line
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'timestamp')  # Перечисляем поля, отображаемые в списке
    search_fields = ['name', 'body']
    list_filter = ('timestamp',)  # Перечисляем поля для фильтрации


# admin.site.register(Article, ArticleAdmin)
