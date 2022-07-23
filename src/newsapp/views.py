from django.shortcuts import render
from newsapi import NewsApiClient

from . import settings_app
from . import models
from . import func_utils
from django.utils.timezone import now

# Create your views here.
def index(request):

  newsapi = NewsApiClient(api_key=settings_app.NEWS_API_KEY)
  top = newsapi.get_top_headlines(sources ='techcrunch')

  l = top['articles']
  desc =[]
  title =[]
  img =[]

  # articles = models.Articles()
  # lst_articles = []

  setting_news = models.SettingNews()

  if setting_news.flag_api:
    for i in range(len(l)):
      f = l[i]
      title.append(f['title'])
      desc.append(f['description'])
      img.append(f['urlToImage'])

      # articles.id_article = func_utils.createIdArticle(f['source']['id'])
      # articles.name = f['source']['name']
      # articles.author = f['author']
      # articles.title = f['title']
      # articles.url_ref_image = f['urlToImage']
      # articles.src_origin = f['url']
      # articles.content = f['content']
      # articles.description = f['description']
      # articles.published_datetime = f['publishedAt']
      # articles.save(force_update=False)

  mylist = zip(title, desc, img)

  return render(request, 'index.html', context ={"mylist":mylist})

def view_news(request):
  articles = models.Articles.objects.all()
  return render(request, 'view_news.html', context ={"articles":articles})
