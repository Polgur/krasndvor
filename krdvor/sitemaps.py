from django.contrib.sitemaps import Sitemap
from dvor.sitemaps import IndexViewSitemap, SectionViewSitemap, StaticViewSitemap, ProjectListTSitemap, \
    ProjectListSSitemap, ProjectListKSitemap, ProjectListT0Sitemap, ProjectListS0Sitemap, ProjectListK0Sitemap, \
    ProjectListT100Sitemap, ProjectListS100Sitemap, ProjectListK100Sitemap, ProjectListT150Sitemap, \
    ProjectListS150Sitemap, ProjectListK150Sitemap, ProjectTSitemap, ProjectSSitemap, ProjectKSitemap, \
    ReadyobjTermoSitemap, ReconstListSitemap, ArticleSitemap, ArticleListSitemap
from django.core.urlresolvers import reverse


class RootSitemap(Sitemap):
    priority = 0.6

    def location(self, url_name):
        return reverse(url_name)


sitemaps = {
    'index': IndexViewSitemap,
    'sections': SectionViewSitemap,
    'static_views': StaticViewSitemap,
    'projects_termo': ProjectListTSitemap,
    'projects_sip': ProjectListSSitemap,
    'projects_karkas': ProjectListKSitemap,
    'projects0_termo': ProjectListT0Sitemap,
    'projects0_sip': ProjectListS0Sitemap,
    'projects0_karkas': ProjectListK0Sitemap,
    'projects100_termo': ProjectListT100Sitemap,
    'projects100_sip': ProjectListS100Sitemap,
    'projects100_karkas': ProjectListK100Sitemap,
    'projects150_termo': ProjectListT150Sitemap,
    'projects150_sip': ProjectListS150Sitemap,
    'projects150_karkas': ProjectListK150Sitemap,
    'project_termo': ProjectTSitemap,
    'project_sip': ProjectSSitemap,
    'project_karkas': ProjectKSitemap,
    'readyobj': ReadyobjTermoSitemap,
    'reconst': ReconstListSitemap,
    'articles': ArticleListSitemap,
    'article': ArticleSitemap,
}
