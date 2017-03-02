from datetime import date

from django.contrib.sitemaps import Sitemap
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from .models import Project, Readyobj, Reconst, Article
from .views import ProjectList, ReadyobjTermo, ReconstList, ArticleList


class IndexViewSitemap(Sitemap):
    priority = 1
    changefreq = 'daily'

    def items(self):
        return ['index_page']

    def location(self, item):
        return reverse(item)


class SectionViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return ['sect_termo', 'sect_sip', 'sect_karkas', 'promo']

    def location(self, item):
        return reverse(item)


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['sect_recon', 'sect_fund', 'sect_remont', 'bstages', 'our_sip', 'our_karkas', 'our_fund', 'expo',
                'contacts']

    def location(self, item):
        return reverse(item)


class ProjectListTSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        objects = Project.objects.filter(techs=1)
        paginator = Paginator(objects, ProjectList.paginate_by)
        return paginator.page_range

    def location(self, page):
        if page > 1:
            return "{}?search=1&vid=0&pmin=0&pmax=5000000&smin=0&smax=500&tech={}&page={}".format(
                reverse("project_list"), 1, page)
        else:
            return "{}?search=1&vid=0&pmin=0&pmax=5000000&smin=0&smax=500&tech={}".format(reverse("project_list"), 1)


class ProjectListSSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        objects = Project.objects.filter(techs=2)
        paginator = Paginator(objects, ProjectList.paginate_by)
        return paginator.page_range

    def location(self, page):
        if page > 1:
            return "{}?search=1&vid=0&pmin=0&pmax=5000000&smin=0&smax=500&tech={}&page={}".format(
                reverse("project_list"), 2, page)
        else:
            return "{}?search=1&vid=0&pmin=0&pmax=5000000&smin=0&smax=500&tech={}".format(reverse("project_list"), 2)


class ProjectListKSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        objects = Project.objects.filter(techs=3)
        paginator = Paginator(objects, ProjectList.paginate_by)
        return paginator.page_range

    def location(self, page):
        if page > 1:
            return "{}?search=1&vid=0&pmin=0&pmax=5000000&smin=0&smax=500&tech={}&page={}".format(
                reverse("project_list"), 3, page)
        else:
            return "{}?search=1&vid=0&pmin=0&pmax=5000000&smin=0&smax=500&tech={}".format(reverse("project_list"), 3)


class ProjectListT0Sitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        objects = Project.objects.filter(techs=1, square__range=(0, 100))
        paginator = Paginator(objects, ProjectList.paginate_by)
        return paginator.page_range

    def location(self, page):
        if page > 1:
            return "{}?search=1&vid=0&pmin=0&pmax=5000000&smin=0&smax=100&tech={}&page={}".format(
                reverse("project_list"), 1, page)
        else:
            return "{}?search=1&vid=0&pmin=0&pmax=5000000&smin=0&smax=100&tech={}".format(reverse("project_list"), 1)

class ProjectListS0Sitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        objects = Project.objects.filter(techs=2, square__range=(0, 100))
        paginator = Paginator(objects, ProjectList.paginate_by)
        return paginator.page_range

    def location(self, page):
        if page > 1:
            return "{}?search=1&vid=0&pmin=0&pmax=5000000&smin=0&smax=100&tech={}&page={}".format(
                reverse("project_list"), 2, page)
        else:
            return "{}?search=1&vid=0&pmin=0&pmax=5000000&smin=0&smax=100&tech={}".format(reverse("project_list"), 2)

class ProjectListK0Sitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        objects = Project.objects.filter(techs=3, square__range=(0, 100))
        paginator = Paginator(objects, ProjectList.paginate_by)
        return paginator.page_range

    def location(self, page):
        if page > 1:
            return "{}?search=1&vid=0&pmin=0&pmax=5000000&smin=0&smax=100&tech={}&page={}".format(
                reverse("project_list"), 3, page)
        else:
            return "{}?search=1&vid=0&pmin=0&pmax=5000000&smin=0&smax=100&tech={}".format(reverse("project_list"), 3)

class ProjectListT100Sitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        objects = Project.objects.filter(techs=1, square__range=(100, 150))
        paginator = Paginator(objects, ProjectList.paginate_by)
        return paginator.page_range

    def location(self, page):
        if page > 1:
            return "{}?search=1&vid=0&pmin=0&pmax=5000000&smin=100&smax=150&tech={}&page={}".format(
                reverse("project_list"), 1, page)
        else:
            return "{}?search=1&vid=0&pmin=0&pmax=5000000&smin=100&smax=150&tech={}".format(reverse("project_list"), 1)

class ProjectListS100Sitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        objects = Project.objects.filter(techs=2, square__range=(100, 150))
        paginator = Paginator(objects, ProjectList.paginate_by)
        return paginator.page_range

    def location(self, page):
        if page > 1:
            return "{}?search=1&vid=0&pmin=0&pmax=5000000&smin=100&smax=150&tech={}&page={}".format(
                reverse("project_list"), 2, page)
        else:
            return "{}?search=1&vid=0&pmin=0&pmax=5000000&smin=100&smax=150&tech={}".format(reverse("project_list"), 2)

class ProjectListK100Sitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        objects = Project.objects.filter(techs=3, square__range=(100, 150))
        paginator = Paginator(objects, ProjectList.paginate_by)
        return paginator.page_range

    def location(self, page):
        if page > 1:
            return "{}?search=1&vid=0&pmin=0&pmax=5000000&smin=100&smax=150&tech={}&page={}".format(
                reverse("project_list"), 3, page)
        else:
            return "{}?search=1&vid=0&pmin=0&pmax=5000000&smin=100&smax=150&tech={}".format(reverse("project_list"), 3)

class ProjectListT150Sitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        objects = Project.objects.filter(techs=1, square__range=(150, 500))
        paginator = Paginator(objects, ProjectList.paginate_by)
        return paginator.page_range

    def location(self, page):
        if page > 1:
            return "{}?search=1&vid=0&pmin=0&pmax=5000000&smin=150&smax=500&tech={}&page={}".format(
                reverse("project_list"), 1, page)
        else:
            return "{}?search=1&vid=0&pmin=0&pmax=5000000&smin=150&smax=5000&tech={}".format(reverse("project_list"), 1)

class ProjectListS150Sitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        objects = Project.objects.filter(techs=2, square__range=(150, 500))
        paginator = Paginator(objects, ProjectList.paginate_by)
        return paginator.page_range

    def location(self, page):
        if page > 1:
            return "{}?search=1&vid=0&pmin=0&pmax=5000000&smin=150&smax=500&tech={}&page={}".format(
                reverse("project_list"), 2, page)
        else:
            return "{}?search=1&vid=0&pmin=0&pmax=5000000&smin=150&smax=500&tech={}".format(reverse("project_list"), 2)

class ProjectListK150Sitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        objects = Project.objects.filter(techs=3, square__range=(150, 500))
        paginator = Paginator(objects, ProjectList.paginate_by)
        return paginator.page_range

    def location(self, page):
        if page > 1:
            return "{}?search=1&vid=0&pmin=0&pmax=5000000&smin=150&smax=500&tech={}&page={}".format(
                reverse("project_list"), 3, page)
        else:
            return "{}?search=1&vid=0&pmin=0&pmax=5000000&smin=150&smax=500&tech={}".format(reverse("project_list"), 3)

class ProjectTSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Project.objects.filter(techs=1)

    def location(self, item):
        return "{}?tech={}".format(reverse("project_detail", kwargs={"slug": item.slug}), 1)

class ProjectSSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Project.objects.filter(techs=2)

    def location(self, item):
        return "{}?tech={}".format(reverse("project_detail", kwargs={"slug": item.slug}), 2)

class ProjectKSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Project.objects.filter(techs=3)

    def location(self, item):
        return "{}?tech={}".format(reverse("project_detail", kwargs={"slug": item.slug}), 3)


class ReadyobjTermoSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        objects = Readyobj.objects.filter(tech=1)
        paginator = Paginator(objects, ReadyobjTermo.paginate_by)
        return paginator.page_range

    def location(self, page):
        if page > 1:
            return "{}?page={}".format(reverse("our_termo"), page)
        else:
            return reverse("our_termo")


class ReconstListSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        objects = Reconst.objects.all()
        paginator = Paginator(objects, ReconstList.paginate_by)
        return paginator.page_range

    def location(self, page):
        if page > 1:
            return "{}?page={}".format(reverse("reconst"), page)
        else:
            return reverse("reconst")


class ArticleListSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        objects = Article.objects.all()
        paginator = Paginator(objects, ArticleList.paginate_by)
        return paginator.page_range

    def location(self, page):
        if page > 1:
            return "{}?page={}".format(reverse("article_list"), page)
        else:
            return reverse("article_list")


class ArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Article.objects.all()

    def lastmod(self, Article):
        return Article.publish

    def location(self, item):
        return reverse("article_detail", kwargs={"slug": item.slug})
