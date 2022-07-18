from django.contrib import admin
from newsapp.models import *

# Register your models here.
# admin.site.register(Articles)
@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
  list_display = ('id_article', 
                  'name', 
                  'title',
                  'type', 
                  'published_at')

# admin.site.register(TypeArticles)
@admin.register(TypeArticles)
class TypeArticlesAdmin(admin.ModelAdmin):
  list_display = ('id_type', 
                  'type')