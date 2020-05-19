from django.shortcuts import render
from future_projects.models import Project

# Create your views here.
def future_index(request):
    projects = Project.objects.all()
    context = {
       'projects': projects
    }
    return render(request, 'future_projects.html', context)


def future_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'future_detail.html', context)
