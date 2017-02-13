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
        item['clss'] = ''
        item['url'] = "{}?{}&tech={}".format(reverse("project_list"), "search=1&vid=0&pmin=0&pmax=5000000&smin=0&smax=500", tech.pk)
        item['slug'] = tech.mnemo
        item['submenu'] = [
            {'name': "До 100 КВ.М", 'clss': '', 'url': "{}?{}&tech={}".format(reverse("project_list"), "search=1&vid=0&pmin=0&pmax=5000000&smin=0&smax=100", tech.pk)},
            {'name': "От 100 до 150 КВ.М", 'clss': '', 'url': "{}?{}&tech={}".format(reverse("project_list"), "search=1&vid=0&pmin=0&pmax=5000000&smin=100&smax=150", tech.pk)},
            {'name': "Свыше 150 КВ.М", 'clss': 'after-divider', 'url': "{}?{}&tech={}".format(reverse("project_list"), "search=1&vid=0&pmin=0&pmax=5000000&smin=150&smax=500", tech.pk)},
            {'name': "divider", 'clss': '', 'url': "{}?{}&tech={}".format(reverse("project_list"), "search=1&vid=0&pmin=0&pmax=5000000&smin=0&smax=100", tech.pk)},
            {'name': "Бани", 'clss': '', 'url': "{}?{}&tech={}".format(reverse("project_list"), "search=1&vid=3&pmin=0&pmax=5000000&smin=0&smax=500", tech.pk)},
            {'name': "Дуплексы", 'clss': '', 'url': "{}?{}&tech={}".format(reverse("project_list"), "search=1&vid=2&pmin=0&pmax=5000000&smin=0&smax=500", tech.pk)},
        ]
        tech_list.append(item)
    return tech_list


menu = [
    {'name': "Главная", 'clss': '', 'url': reverse("index_page"), 'slug': 'home'},
    {'name': "Технологии", 'clss': '', 'url': '#', 'slug': 'techs', 'submenu':
        [
            {'name': "Термопанели", 'clss': '', 'url': '#', 'slug': 'techs_1'},
            {'name': "СИП панели", 'clss': '', 'url': '#', 'slug': 'techs_2'},
            {'name': "Каркасные", 'clss': 'after-divider', 'url': '#', 'slug': 'techs_3'},
            {'name': "divider", 'clss': '', 'url': '#', 'slug': ''},
            {'name': "Реконструкции", 'clss': '', 'url': '#', 'slug': 'rec'},
            {'name': "Фундаменты", 'clss': '', 'url': '#', 'slug': 'fun'},
            {'name': "Ремонт и отделка", 'clss': '', 'url': '#', 'slug': 'rem'},
        ]},
    {'name': "Проекты", 'clss': '', 'url': '#', 'slug': 'projects', 'submenu': get_tech()},
    {'name': "Наши объекты", 'clss': '', 'url': '#', 'slug': 'techs', 'submenu':
        [
            {'name': "Этапы строительства", 'clss': 'after-divider', 'url': '#', 'slug': 'techs_3'},
            {'name': "divider", 'clss': '', 'url': '#', 'slug': ''},
            {'name': "Термопанели", 'clss': '', 'url': '#', 'slug': 'techs_1'},
            {'name': "СИП панели", 'clss': '', 'url': '#', 'slug': 'techs_2'},
            {'name': "Каркасные", 'clss': 'after-divider', 'url': '#', 'slug': 'techs_3'},
            {'name': "divider", 'clss': '', 'url': '#', 'slug': ''},
            {'name': "Реконструкции", 'clss': '', 'url': '#', 'slug': 'rec'},
            {'name': "Фундаменты", 'clss': 'after-divider', 'url': '#', 'slug': 'fun'},
            {'name': "divider", 'clss': '', 'url': '#', 'slug': ''},
            {'name': "Дома на продажу", 'clss': '', 'url': '#', 'slug': 'rem'},
        ]},
    {'name': "Информация", 'clss': '', 'url': '#', 'slug': 'info', 'submenu':
        [
            {'name': "Вопросы и ответы", 'clss': '', 'url': '#', 'slug': 'questions'},
            {'name': "Статьи", 'clss': '', 'url': reverse("article_list"), 'slug': 'articles'},
            {'name': "Сертификаты", 'clss': '', 'url': '#', 'slug': 'certif'},
        ]},
    {'name': "Отзывы", 'clss': '', 'url': '#', 'slug': 'feedback'},
    {'name': "Контакты", 'clss': '', 'url': '#', 'slug': 'contacts'},
]

@register.inclusion_tag('includes/menu.html')
def menu_render(request, slug):
    return {'request': request, 'menu': menu, 'menu_slug': slug}