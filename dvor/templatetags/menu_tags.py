from django import template
from django.core.urlresolvers import reverse

register = template.Library()

menu = [
  {'name': "Главная", 'url': reverse("index_page"), 'slug': 'home'},
  {'name': "Проекты", 'url': '#', 'slug': 'projects', 'submenu':
    [
      {'name': "Термопанели", 'url': '#', 'submenu':[
        {'name': "До 100 КВ.М", 'url': "{}?{}".format(reverse("project_list"), "smin=0&smax=100")},
        {'name': "От 100 до 150 КВ.М", 'url': "{}?{}".format(reverse("project_list"), "smin=100&smax=150")},
      ]},
    ]}
]

@register.inclusion_tag('includes/menu.html')
def menu_render(request, slug):
    return {'request': request, 'menu': menu, 'menu_slug': slug}