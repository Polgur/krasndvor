from django.conf.urls import url
from . import views
from .views import ProjectList, ProjectDetail
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^projects/$', ProjectList.as_view(), name='project_list'),
    url(r'^projects/(?P<slug>[^/]*)$', ProjectDetail.as_view(), name='project_detail'),
]

urlpatterns += [
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT, }),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)