from django.contrib.sitemaps import Sitemap
from dvor.sitemaps import ArticleSitemap, ArticleListSitemap
from django.core.urlresolvers import reverse

class RootSitemap(Sitemap):
    priority = 0.6

    def location(self, url_name):
        return reverse(url_name)

sitemaps = {
    'article': ArticleSitemap,
    'articles': ArticleListSitemap,
}