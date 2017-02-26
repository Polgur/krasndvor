from django.conf.urls import url
from .views import IndexPage, SectionTermo, SectionSip, SectionKarkas, SectionRecon, SectionFund, SectionRemont, \
    OurStages, OurSip, OurKarkas, OurFund, ContactsPage, ProjectList, ProjectDetail, ReadyobjTermo, ReconstList, ExpoDom, Promo, \
    ArticleList, ArticleDetail, MainCalcView, PrjCalcView, PhoneCallView
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^$', IndexPage.as_view(), name='index_page'),
    url(r'^termopanel/$', SectionTermo.as_view(), name='sect_termo'),
    url(r'^sip-panel/$', SectionSip.as_view(), name='sect_sip'),
    url(r'^karkasnie-doma/$', SectionKarkas.as_view(), name='sect_karkas'),
    url(r'^reconstrukcii/$', SectionRecon.as_view(), name='sect_recon'),
    url(r'^fundament/$', SectionFund.as_view(), name='sect_fund'),
    url(r'^remont-otdelka/$', SectionRemont.as_view(), name='sect_remont'),
    url(r'^build-stages/$', OurStages.as_view(), name='bstages'),
    url(r'^our-termopanel/$', ReadyobjTermo.as_view(), name='our_termo'),
    url(r'^our-sip-panel/$', OurSip.as_view(), name='our_sip'),
    url(r'^our-kaskasnie-doma/$', OurKarkas.as_view(), name='our_karkas'),
    url(r'^reconstruction/$', ReconstList.as_view(), name='reconst'),
    url(r'^fundament-gallery/$', OurFund.as_view(), name='our_fund'),
    url(r'^vystavochnyj/$', ExpoDom.as_view(), name='expo'),
    url(r'^contacts/$', ContactsPage.as_view(), name='contacts'),
    url(r'^projects/$', ProjectList.as_view(), name='project_list'),
    url(r'^projects/(?P<slug>[^/]*)$', ProjectDetail.as_view(), name='project_detail'),
    url(r'^promotion/$', Promo.as_view(), name='promo'),
    url(r'^articles/$', ArticleList.as_view(), name='article_list'),
    url(r'^articles/(?P<slug>[^/]*)$', ArticleDetail.as_view(), name='article_detail'),
    url(r'^thanks/$', MainCalcView.as_view(), name='thanks'),
    url(r'^thanks_p/$', PrjCalcView.as_view(), name='thanks_prj'),
    url(r'^thanks_call/$', PhoneCallView.as_view(), name='thanks_call'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
        url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT, }),
    ]
