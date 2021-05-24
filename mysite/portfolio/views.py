from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'classhome': "nav-current"}
    return render(request, 'portfolio/new/index.html',context)

def about(request):
    context = {'classhome': "nav-current"}
    return render(request, 'portfolio/new/about.html',context)

def products(request):
    context = {'classhome': "nav-current"}
    return render(request, 'portfolio/new/products.html',context)

def shop(request):
    context = {'classhome': "nav-current"}
    return render(request, 'portfolio/new/shop.html',context)

