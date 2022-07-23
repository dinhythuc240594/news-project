from django.contrib import admin
from newsapp.models import *

# Register your models here.
# admin.site.register(Articles)
@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
  list_display = ('id_article', 
                  'category_article',
                  'title',
                  'show_types', 
                  'published_at')

  def show_types(self, obj):
    return ", ".join([a.type for a in obj.type.all()])

# admin.site.register(TypeArticles)
@admin.register(TypeArticles)
class TypeArticlesAdmin(admin.ModelAdmin):
  list_display = ('id_type', 
                  'type')

# admin.site.register(SettingNews)