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
            #{'name': "divider", 'clss': '', 'url': "{}?{}&tech={}".format(reverse("project_list"), "search=1&vid=0&pmin=0&pmax=5000000&smin=0&smax=100", tech.pk)},
            #{'name': "Бани", 'clss': '', 'url': "{}?{}&tech={}".format(reverse("project_list"), "search=1&vid=3&pmin=0&pmax=5000000&smin=0&smax=500", tech.pk)},
            #{'name': "Дуплексы", 'clss': '', 'url': "{}?{}&tech={}".format(reverse("project_list"), "search=1&vid=2&pmin=0&pmax=5000000&smin=0&smax=500", tech.pk)},
        ]
        tech_list.append(item)
    return tech_list


menu = [
    {'name': "Главная", 'clss': '', 'url': reverse("index_page"), 'slug': 'home'},
    {'name': "Технологии", 'clss': '', 'url': '#', 'slug': 'techs', 'submenu':
        [
            {'name': "Термопанели", 'clss': '', 'url': reverse("sect_termo"), 'slug': 'sect_termo'},
            {'name': "СИП панели", 'clss': '', 'url': reverse("sect_sip"), 'slug': 'sect_sip'},
            {'name': "Каркасные", 'clss': 'after-divider', 'url': reverse("sect_karkas"), 'slug': 'sect_karkas'},
            {'name': "divider", 'clss': '', 'url': '#', 'slug': ''},
            {'name': "Реконструкции", 'clss': '', 'url': reverse("sect_recon"), 'slug': 'sect_recon'},
            {'name': "Фундаменты", 'clss': '', 'url': reverse("sect_fund"), 'slug': 'sect_fund'},
            {'name': "Ремонт и отделка", 'clss': '', 'url': reverse("sect_remont"), 'slug': 'sect_remont'},
        ]},
    {'name': "Проекты", 'clss': '', 'url': '#', 'slug': 'projects', 'submenu': get_tech()},
    {'name': "Наши объекты", 'clss': '', 'url': '#', 'slug': 'our_obj', 'submenu':
        [
            {'name': "Этапы строительства", 'clss': 'after-divider', 'url': reverse("bstages"), 'slug': 'bstages'},
            {'name': "divider", 'clss': '', 'url': '#', 'slug': ''},
            {'name': "Термопанели", 'clss': '', 'url': reverse("our_termo"), 'slug': 'our_termo'},
            {'name': "СИП панели", 'clss': '', 'url': reverse("our_sip"), 'slug': 'our_sip'},
            {'name': "Каркасные", 'clss': 'after-divider', 'url': reverse("our_karkas"), 'slug': 'our_karkas'},
            {'name': "divider", 'clss': '', 'url': '#', 'slug': ''},
            {'name': "Реконструкции", 'clss': '', 'url': reverse("reconst"), 'slug': 'reconst'},
            {'name': "Фундаменты", 'clss': 'after-divider', 'url': reverse("our_fund"), 'slug': 'our_fund'},
            {'name': "divider", 'clss': '', 'url': '#', 'slug': ''},
            #{'name': "Дома на продажу", 'clss': '', 'url': '#', 'slug': 'rem'},
            {'name': "Выставочный дом", 'clss': '', 'url': reverse("expo"), 'slug': 'expo'},
        ]},
    {'name': "Информация", 'clss': '', 'url': '#', 'slug': 'info', 'submenu':
        [
            #{'name': "Вопросы и ответы", 'clss': '', 'url': '#', 'slug': 'questions'},
            {'name': "Акции", 'clss': '', 'url': reverse("promo"), 'slug': 'promo'},
            {'name': "Статьи", 'clss': '', 'url': reverse("article_list"), 'slug': 'articles'},
            {'name': "Сертификаты", 'clss': '', 'url': reverse("certif"), 'slug': 'certif'},
        ]},
    {'name': "Отзывы", 'clss': '', 'url': reverse("review"), 'slug': 'review'},
    {'name': "Контакты", 'clss': '', 'url': reverse("contacts"), 'slug': 'contacts'},
]

@register.inclusion_tag('includes/menu.html')
def menu_render(request, slug):
    return {'request': request, 'menu': menu, 'menu_slug': slug}