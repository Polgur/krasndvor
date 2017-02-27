from django.http import Http404
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from .models import Project, PrjKit, Readyobj, Reconst, Article, Techno, Calculation, PhoneCall
from .forms import ProjectFilterForm, MainCalc, PrjCalc, FundCalc, PhoneForm
from .utils import MenuMixin, jsonify
from django.core.mail import send_mail


# Create your views here.
class IndexPage(MenuMixin,TemplateView):
    menu_slug = 'home'
    template_name = 'dvor/index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['projects'] = Project.objects.filter(name__in=['Ольгово','Дубровицы','Никольское']).order_by('square')
        return ctx


class SectionTermo(MenuMixin,TemplateView):
    menu_slug = [
        "techs",
        "sect_termo",
    ]
    template_name = 'dvor/sect_termo.html'

class SectionSip(MenuMixin,TemplateView):
    menu_slug = [
        "techs",
        "sect_sip",
    ]
    template_name = 'dvor/sect_sip.html'

class SectionKarkas(MenuMixin,TemplateView):
    menu_slug = [
        "techs",
        "sect_karkas",
    ]
    template_name = 'dvor/sect_karkas.html'

class SectionRecon(MenuMixin,TemplateView):
    menu_slug = [
        "techs",
        "sect_recon",
    ]
    template_name = 'dvor/sect_recon.html'

class SectionFund(MenuMixin,TemplateView):
    menu_slug = [
        "techs",
        "sect_fund",
    ]
    template_name = 'dvor/sect_fund.html'

class SectionRemont(MenuMixin,TemplateView):
    menu_slug = [
        "techs",
        "sect_remont",
    ]
    template_name = 'dvor/sect_remont.html'

class OurStages(MenuMixin,TemplateView):
    menu_slug = [
        "our_obj",
        "bstages",
    ]
    template_name = 'dvor/our_stages.html'

class OurSip(MenuMixin,TemplateView):
    menu_slug = [
        "our_obj",
        "our_sip",
    ]
    template_name = 'dvor/our_sip.html'

class OurKarkas(MenuMixin,TemplateView):
    menu_slug = [
        "our_obj",
        "our_karkas",
    ]
    template_name = 'dvor/our_karkas.html'

class OurFund(MenuMixin,TemplateView):
    menu_slug = [
        "our_obj",
        "our_fund",
    ]
    template_name = 'dvor/our_fund.html'

class ContactsPage(MenuMixin,TemplateView):
    menu_slug = 'contacts'
    template_name = 'dvor/contacts.html'


class ProjectList(MenuMixin,ListView):
    model = Project
    techfilter = None
    paginate_by = 21
    menu_slug = [
        "projects",
    ]

    search_form_class = ProjectFilterForm
    search_form = None

    def get(self, request, *args, **kwargs):
        if request.GET.get('search'):
            self.search_form = self.search_form_class(request.GET)
            if self.search_form.is_valid():
                self.queryset = Project.objects.filter(
                    square__range=(self.search_form.cleaned_data.get('smin'),self.search_form.cleaned_data.get('smax')),
                    price__range=(self.search_form.cleaned_data.get('pmin'),self.search_form.cleaned_data.get('pmax')))
                if self.search_form.cleaned_data.get('vid') != '0':
                    self.queryset = self.queryset.filter(vid__exact=self.search_form.cleaned_data.get('vid'))
                if self.search_form.cleaned_data.get('tech'):
                    self.techfilter = self.search_form.cleaned_data.get('tech')
                    self.queryset = self.queryset.filter(techs=self.search_form.cleaned_data.get('tech'))
                else:
                    self.techfilter = Techno.objects.filter(mnemo='Термопанели').first()
                    self.queryset = self.queryset.filter(techs=self.techfilter)
                self.queryset = self.queryset.order_by('square')
        else:
            self.techfilter = Techno.objects.filter(mnemo='Термопанели').first()
            self.search_form = self.search_form_class()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        self.menu_slug.clear()
        self.menu_slug.append("projects")
        self.menu_slug.append(self.techfilter.mnemo)
        ctx['search_form'] = self.search_form
        ctx['techfilter'] = self.techfilter
        ctx['menu_slug'] = self.menu_slug
        return ctx

class ProjectDetail(DetailView):
    template_name = 'dvor/project_detail.html'

    def get_object(self, queryset=None):
        try:
            if self.request.GET.get('tech'):
                project = Project.objects.prefetch_related('photos').get(slug=self.kwargs.get('slug'),
                techs__pk = self.request.GET.get('tech'))
            else:
                techfilter = Techno.objects.filter(mnemo='Термопанели').first()
                project = Project.objects.prefetch_related('photos').get(slug=self.kwargs.get('slug'),
                techs__pk=techfilter.pk)
            return project
        except Project.DoesNotExist:
            raise Http404('Проект не найден')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        if self.request.GET.get('tech'):
            self.tech = Techno.objects.filter(pk=self.request.GET.get('tech')).first()
        else:
            self.tech = Techno.objects.filter(mnemo='Термопанели').first()
        ctx['kit'] = self.object.kits.filter(tech=self.tech).first()
        ctx['techfilter'] = self.tech
        return ctx

class ReadyobjTermo(MenuMixin,ListView):
    queryset = Readyobj.objects.filter(tech=1).order_by('photos__sort','photos__prn')
    paginate_by = 3
    menu_slug = [
        "our_obj",
        "our_termo",
    ]
    template_name = 'dvor/our_termo.html'

class ReconstList(MenuMixin,ListView):
    queryset = Reconst.objects.all().order_by('photos__sort', 'sort_re', 'photos__prn')
    paginate_by = 6
    menu_slug = [
        "our_obj",
        "reconst",
    ]
    template_name = 'dvor/reconst.html'


class ExpoDom(MenuMixin,TemplateView):
    menu_slug = [
        "our_obj",
        "expo",
    ]
    template_name = 'dvor/expodom.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['expo'] = Readyobj.objects.filter(mnemo='Мичурино').order_by('photos__sort').first()
        return ctx

class Promo(MenuMixin,TemplateView):
    menu_slug = [
        "info",
        "promo",
    ]
    template_name = 'dvor/promo.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['projects_term'] = Project.objects.filter(name__in=['Ольгово','Дубровицы','Никольское']).order_by('square')
        ctx['projects_sip']  = Project.objects.filter(name__in=['Подушкино','Марфино','Аполье']).order_by('square')
        ctx['projects_kars'] = Project.objects.filter(name__in=['Киреево','Дарьино','Мелихово']).order_by('square')
        return ctx


class ArticleList(MenuMixin,ListView):
    model = Article
    paginate_by = 10
    menu_slug = [
        "info",
        "articles",
    ]

class ArticleDetail(MenuMixin,DetailView):
    model = Article
    menu_slug = [
        "info",
        "articles",
    ]

class MainCalcView(CreateView):
    form_class = MainCalc
    model = Calculation
    template_name = 'dvor/thanks.html'

    def form_valid(self, form):
        form.save()
        message = "Данные отправителя:\nФИО: {}".format(form.cleaned_data.get('fio'))
        if form.cleaned_data.get('email'):
            message += "\nemail: {}".format(form.cleaned_data.get('email'))
        if form.cleaned_data.get('phone'):
            message += "\nТелефон: {}".format(form.cleaned_data.get('phone'))
        if form.cleaned_data.get('file'):
            message += "\nк заявке прикреплен файл (его можно посмотреть на сайте)"
        message += "\n\n Пожелания: \n{}".format(form.cleaned_data.get('note'))
        send_mail(
            subject = 'Заявка на расчет ({} {})'.format(form.cleaned_data.get('fio'),form.cleaned_data.get('phone')),
            message = message,
            from_email = 'lagumor@inbox.ru',
            recipient_list = ['lagumor@inbox.ru'],
        )
        return jsonify({'status': 1, 'errors': None})

    def form_invalid(self, form):
        return jsonify({'status': 0, 'errors': form.errors})

class PrjCalcView(CreateView):
    form_class = PrjCalc
    model = Calculation
    template_name = 'dvor/thanks.html'

    def form_valid(self, form):
        form.save()
        kit = PrjKit.objects.filter(pk=form.cleaned_data.get('kit').id).first()
        kit_name = "{} {}".format(kit.prn.name.title(),kit.tech.mnemo.title())
        if form.cleaned_data.get('kit_numb') == 1:
            kit_calc = "комфорт"
        else:
            kit_calc = "премиум"
        message = "Данные отправителя:\nФИО: {}".format(form.cleaned_data.get('fio'))
        if form.cleaned_data.get('email'):
            message += "\nemail: {}".format(form.cleaned_data.get('email'))
        if form.cleaned_data.get('phone'):
            message += "\nТелефон: {}".format(form.cleaned_data.get('phone'))
        if form.cleaned_data.get('file'):
            message += "\nк заявке прикреплен файл (его можно посмотреть на сайте)"
        message += "\n\n Пожелания: \n{}".format(form.cleaned_data.get('note'))
        send_mail(
            subject = 'Заявка на проект {}, комплектация: {} ({} {})'.format(kit_name, kit_calc, form.cleaned_data.get('fio'),form.cleaned_data.get('phone')),
            message = message,
            from_email = 'lagumor@inbox.ru',
            recipient_list = ['lagumor@inbox.ru'],
        )
        return jsonify({'status': 1, 'errors': None})

    def form_invalid(self, form):
        return jsonify({'status': 0, 'errors': form.errors})

class FundCalcView(CreateView):
    form_class = FundCalc
    model = Calculation
    template_name = 'dvor/thanks.html'

    def form_valid(self, form):
        form.save()
        message = "Данные отправителя:\nФИО: {}".format(form.cleaned_data.get('fio'))
        if form.cleaned_data.get('email'):
            message += "\nemail: {}".format(form.cleaned_data.get('email'))
        if form.cleaned_data.get('phone'):
            message += "\nТелефон: {}".format(form.cleaned_data.get('phone'))
        if form.cleaned_data.get('file'):
            message += "\nк заявке прикреплен файл (его можно посмотреть на сайте)"
        message += "\n\n Пожелания: \n{}".format(form.cleaned_data.get('note'))
        send_mail(
            subject = 'Заявка на расчет фундамента ({} {})'.format(form.cleaned_data.get('fio'),form.cleaned_data.get('phone')),
            message = message,
            from_email = 'lagumor@inbox.ru',
            recipient_list = ['lagumor@inbox.ru'],
        )
        return jsonify({'status': 1, 'errors': None})

    def form_invalid(self, form):
        return jsonify({'status': 0, 'errors': form.errors})

class PhoneCallView(CreateView):
    form_class = PhoneForm
    model = PhoneCall
    template_name = 'dvor/thanks.html'

    def form_valid(self, form):
        form.save()
        message = "Данные отправителя:\nФИО: {}".format(form.cleaned_data.get('fio'))
        if form.cleaned_data.get('email'):
            message += "\nemail: {}".format(form.cleaned_data.get('email'))
        message += "\nТелефон: {}".format(form.cleaned_data.get('phone'))
        if form.cleaned_data.get('wtime'):
          message += "\nВремя звонка: {}".format(form.cleaned_data.get('wtime'))
        send_mail(
            subject = 'Обратный звонок ({} {})'.format(form.cleaned_data.get('fio'),form.cleaned_data.get('phone')),
            message = message,
            from_email = 'lagumor@inbox.ru',
            recipient_list = ['lagumor@inbox.ru'],
        )
        return jsonify({'status': 1, 'errors': None})

    def form_invalid(self, form):
        return jsonify({'status': 0, 'errors': form.errors})