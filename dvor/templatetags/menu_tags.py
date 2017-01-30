from django import template
from django.core.urlresolvers import reverse
from ..models import Techno

register = template.Library()

def get_tech():
    tech_list = list()
    techs = Techno.objects.filter(show_in_menu=True)
    for tech in techs:
        item = dict()
        item['name'] = tech.mnemo
        item['url'] = "{}?{}&tech={}".format(reverse("project_list"), "search=1&vid=0&pmin=0&pmax=5000000&smin=0&smax=500", tech.pk)
        item['slug'] = tech.mnemo
        item['submenu'] = [
            {'name': "До 100 КВ.М", 'url': "{}?{}&tech={}".format(reverse("project_list"), "search=1&vid=0&pmin=0&pmax=5000000&smin=0&smax=100", tech.pk)},
            {'name': "От 100 до 150 КВ.М", 'url': "{}?{}&tech={}".format(reverse("project_list"), "search=1&vid=0&pmin=0&pmax=5000000&smin=100&smax=150", tech.pk)},
            {'name': "Свыше 150 КВ.М", 'url': "{}?{}&tech={}".format(reverse("project_list"), "search=1&vid=0&pmin=0&pmax=5000000&smin=150&smax=500", tech.pk)},
            {'name': "divider", 'url': "{}?{}&tech={}".format(reverse("project_list"), "search=1&vid=0&pmin=0&pmax=5000000&smin=0&smax=100", tech.pk)},
            {'name': "Бани", 'url': "{}?{}&tech={}".format(reverse("project_list"), "search=1&vid=3&pmin=0&pmax=5000000&smin=0&smax=500", tech.pk)},
            {'name': "Дуплексы", 'url': "{}?{}&tech={}".format(reverse("project_list"), "search=1&vid=2&pmin=0&pmax=5000000&smin=0&smax=500", tech.pk)},
        ]
        tech_list.append(item)
    return tech_list


menu = [
    {'name': "Главная", 'url': reverse("index_page"), 'slug': 'home'},
    {'name': "Технологии", 'url': '#', 'slug': 'techs', 'submenu':
        [
            {'name': "Термопанели", 'url': '#', 'slug': 'techs_1'},
            {'name': "СИП панели", 'url': '#', 'slug': 'techs_2'},
            {'name': "Каркасные", 'url': '#', 'slug': 'techs_3'},
            {'name': "divider", 'url': '#', 'slug': ''},
            {'name': "Реконструкции", 'url': '#', 'slug': 'rec'},
            {'name': "Фундаменты", 'url': '#', 'slug': 'fun'},
            {'name': "Ремонт и отделка", 'url': '#', 'slug': 'rem'},
        ]},
    {'name': "Проекты", 'url': '#', 'slug': 'projects', 'submenu': get_tech()},
    {'name': "Наши объекты", 'url': '#', 'slug': 'techs', 'submenu':
        [
            {'name': "Этапы строительства", 'url': '#', 'slug': 'techs_3'},
            {'name': "divider", 'url': '#', 'slug': ''},
            {'name': "Термопанели", 'url': '#', 'slug': 'techs_1'},
            {'name': "СИП панели", 'url': '#', 'slug': 'techs_2'},
            {'name': "Каркасные", 'url': '#', 'slug': 'techs_3'},
            {'name': "divider", 'url': '#', 'slug': ''},
            {'name': "Реконструкции", 'url': '#', 'slug': 'rec'},
            {'name': "Фундаменты", 'url': '#', 'slug': 'fun'},
            {'name': "divider", 'url': '#', 'slug': ''},
            {'name': "Дома на продажу", 'url': '#', 'slug': 'rem'},
        ]},
    {'name': "Информация", 'url': '#', 'slug': 'info', 'submenu':
        [
            {'name': "Вопросы и ответы", 'url': '#', 'slug': 'questions'},
            {'name': "Статьи", 'url': reverse("article_list"), 'slug': 'articles'},
            {'name': "Сертификаты", 'url': '#', 'slug': 'certif'},
        ]},
    {'name': "Отзывы", 'url': '#', 'slug': 'feedback'},
    {'name': "Контакты", 'url': '#', 'slug': 'contacts'},
]

@register.inclusion_tag('includes/menu.html')
def menu_render(request, slug):
    return {'request': request, 'menu': menu, 'menu_slug': slug}