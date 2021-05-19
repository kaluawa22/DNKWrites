from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'classhome': "nav-current"}
    return render(request, 'portfolio/index.html',context)