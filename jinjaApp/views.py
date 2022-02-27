from django.shortcuts import render
from .models import Product
# Create your views here.

def index(request):
    return render(request, 'home.html')

def home_view (request):
    obj = Product.objects.all

    # if request.method == "POST":
    # obj.delete()
    # context = {
    #     "object": obj
    # }
    # return HttpResponse("<h1>Hello world</h1>")
    return render(request, 'display.html')