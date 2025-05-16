from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'menu/index.html')

def home(request):
    return render(request, 'menu/home.html')

def about(request):
    return render(request, 'menu/about.html')

def contacts(request):
    return render(request, 'menu/contacts.html')

def services(request):
    return render(request, 'menu/services.html')    

def products(request):
    return render(request, 'menu/products.html')

def news(request):
    return render(request, 'menu/news.html')



