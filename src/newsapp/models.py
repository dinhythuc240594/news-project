from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Articles(models.Model):
  id_article = models.CharField(max_length=10, default='')
  name = models.TextField()
  title = models.TextField()
  type = models.ForeignKey('TypeArticles',on_delete=models.CASCADE,default='')
  author = models.TextField()
  published_at = models.DateField()
  url_ref_image = models.TextField()
  src_origin = models.TextField()
  description = models.TextField()
  content = HTMLField(default='')

  # class Meta:
  #   db_table='articles'

  def __str__(self):
    return self.title 

class TypeArticles(models.Model):
  id_type = models.CharField(max_length=10, default='')
  type = models.TextField()

  # class Meta:
  #   db_table='typearticles'
  
  def __str__(self):
    return self.type 