# from .urls import urlpatterns as homeUrls
from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse

class StaticSitemap(Sitemap):
     priority = 0.8
     changefreq = 'weekly'

     # The below method returns all urls defined in urls.py file
    #  def items(self):
    #     mylist = [ ]
    #     for url in homeUrls:
    #         mylist.append('home:'+url.name) 
    #     return mylist

    #  def location(self, item):
        #  return reverse(item)