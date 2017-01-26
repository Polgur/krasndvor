from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Project, Article, Techno
from .forms import ProjectFilterForm

# Create your views here.
class IndexPage(TemplateView):
    template_name = 'dvor/index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['projects'] = Project.objects.all()[:3]
        return ctx


class ProjectList(ListView):
    model = Project
    techfilter = None
    paginate_by = 18

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
                    self.techfilter = Techno.objects.filter(mnemo='Термопанели')
                    self.queryset = self.queryset.filter(techs=self.techfilter)
        else:
            self.techfilter = Techno.objects.filter(mnemo='Термопанели')
            self.search_form = self.search_form_class()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['search_form'] = self.search_form
        ctx['techfilter'] = self.techfilter
        return ctx


class ProjectDetail(DetailView):
    queryset = Project.objects.all().prefetch_related('photos')

class ArticleList(ListView):
    model = Article
    paginate_by = 10

class ArticleDetail(DetailView):
    model = Article