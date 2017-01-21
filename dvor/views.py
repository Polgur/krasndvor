from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Project, Article
# Create your views here.
class IndexPage(TemplateView):
    template_name = 'dvor/index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['projects'] = Project.objects.all()[:3]
        return ctx

class ProjectList(ListView):
    model = Project
    paginate_by = 18

class ProjectDetail(DetailView):
    queryset = Project.objects.all().prefetch_related('Photos')

class ArticleList(ListView):
    model = Article
    paginate_by = 10

class ArticleDetail(DetailView):
    model = Article