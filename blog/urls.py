from django.urls import path
from blog.views import *
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from blog.feeds import LatestEntriesFeed


app_name = 'blog'

urlpatterns = [
    path('',blog_view,name='index'),
    path('<int:pid>',blog_single,name='single'),
    path("rss/feed/", LatestEntriesFeed()),
  
    ]
