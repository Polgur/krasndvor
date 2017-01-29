from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Project, Article, Techno
from .forms import ProjectFilterForm
from .utils import MenuMixin


# Create your views here.
class IndexPage(MenuMixin,TemplateView):
    menu_slug = 'home'
    template_name = 'dvor/index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['projects'] = Project.objects.all()[:3]
        return ctx


class ProjectList(MenuMixin,ListView):
    model = Project
    techfilter = None
    paginate_by = 18
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
