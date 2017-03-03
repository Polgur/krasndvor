"""krdvor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse
from dvor.views import YandexVerificationView
from django.contrib.sitemaps.views import (
    index as site_index_view,
    sitemap as sitemap_view)
from .sitemaps import sitemaps as sitemaps_dict

urlpatterns = [
    url(r'^', include('dvor.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^googlec3d802055a2219fc\.html$', lambda r: HttpResponse("google-site-verification: googlec3d802055a2219fc.html", content_type="text/plain")),
    url(
        r'^yandex_4fd6f02cc008408c\.html$',
        YandexVerificationView.as_view(),
        name='yandex_verify'
    ),
    url(r'^sitemap\.xml$',
        sitemap_view,
        {'sitemaps': sitemaps_dict},
        name='sitemap-sections'),
]
