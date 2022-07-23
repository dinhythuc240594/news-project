from django.db import models
from . import func_utils
from tinymce.models import HTMLField
from django.utils.timezone import now
import base64
from io import BytesIO

# Create your models here.
class Articles(models.Model):
  id_article = models.CharField(max_length=50, default='', editable=False)
  category_article = models.CharField(max_length=50, default='')
  title = models.CharField(max_length=100, default='')
  type = models.ManyToManyField('TypeArticles',default='')
  author = models.CharField(max_length=50, default='')
  published_at = models.DateField(default=now)
  published_time = models.TimeField(default=now)
  image = models.ImageField(upload_to = 'images' , default = 'demo/demo.png')
  thumbnail = models.CharField(max_length=2000, blank=True, null=True)
  description = models.TextField(blank=True)
  content = HTMLField(default='', blank=True)

  def save(self, *args, **kwargs):

    if not self.image:
      self.thumbnail = None
    else:
      thumbnail_size = 50, 50
      data_img = BytesIO()
      tiny_img = Articles.open(self.image)
      tiny_img.thumbnail(thumbnail_size)
      tiny_img.save(data_img, format="BMP")
      tiny_img.close()
      try:
        self.thumbnail = "data:image/jpg;base64,{}".format(
            base64.b64encode(data_img.getvalue()).decode("utf-8")
        )
      except UnicodeDecodeError:
        self.blurred_image = None

    self.id_article = func_utils.createIdArticle()
    super(Articles, self).save(*args, **kwargs)

  # class Meta:
  #   db_table='articles'

  def __str__(self):
    return self.title 


class TypeArticles(models.Model):
  id_type = models.CharField(max_length=10, default='')
  type = models.CharField(max_length=20, default='')
  published_at = models.DateField(default=now)

  # class Meta:
  #   db_table='typearticles'
  
  def __str__(self):
    return self.type 


class SettingNews(models.Model):
  flag_api = models.BooleanField(default=True)
