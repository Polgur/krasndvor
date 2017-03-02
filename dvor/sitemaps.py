from datetime import date

from django.contrib.sitemaps import Sitemap
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from .models import Article
from .views import ArticleList


class ArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Article.objects.all()

    def lastmod(self, Article):
        return Article.publish

    def location(self, item):
        return reverse("article_detail", kwargs={"slug": item.slug})

class ArticleListSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        objects = Article.objects.all()
        paginator = Paginator(objects, ArticleList.paginate_by)
        return paginator.page_range

    def location(self, page):
        if page > 1:
            return "{}?page={}".format(reverse("article_list"),page)
        else:
            return reverse("article_list")
