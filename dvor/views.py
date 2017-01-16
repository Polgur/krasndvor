from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Project
# Create your views here.
def main_page(request):
    return render(request, 'dvor/index.html')

class ProjectList(ListView):
    model = Project
    paginate_by = 18

class ProjectDetail(DetailView):
    queryset = (
        Project.objects
    )