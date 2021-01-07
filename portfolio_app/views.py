from django.shortcuts import render
from portfolio_app.models import Portfolio

# Create your views here.
def base(request):
    return render(request, "html/base.html", {})

def home(request):
    return render(request, "html/home.html", {})

def about(request):
    return render(request, "html/about.html", {})

def resume(request):
    return render(request, "html/resume.html", {})

def portfolio_index(request):
    projects = Portfolio.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'html/portfolio_index.html', context)

def portfolio_detail(request, pk):
    project = Portfolio.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'html/portfolio_detail.html', context)

def contact(request):
    return render(request, "html/contact.html", {})
