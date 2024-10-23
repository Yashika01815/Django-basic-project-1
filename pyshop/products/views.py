from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
#here django is a package shorcuts is the module and render is the function
# Create your views here.
#writting a view function ie index
# /products -> index
#index is used as bydefault like if we write products in the website then it will lead to the content written in index but if write products/instruction then it will show the content of instruction function 
def index(request):
 products=Product.objects.all()
 return render (request, 'index.html',
                {'products':products})


def instruction(request):
 return HttpResponse('for integration content of python to the website we use framworks and here we are using django.first add content to view.py then url.py and then url.py of products')