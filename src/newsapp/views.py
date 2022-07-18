from django.shortcuts import render
from newsapi import NewsApiClient

from . import settings_app

# Create your views here.
def index(request):

    newsapi = NewsApiClient(api_key =settings_app.NEWS_API_KEY)
    top = newsapi.get_top_headlines(sources ='techcrunch')

    l = top['articles']
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)

    return render(request, 'index.html', context ={"mylist":mylist})