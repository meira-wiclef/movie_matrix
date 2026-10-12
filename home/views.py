from django.shortcuts import render
from pip._internal import index


# Create your views here.
def home(request):
    return render(request,'home/index.html')

def movie(request):
    return render(request,'home/movie.html')

def about(request):
    return render(request,'home/aboutus.html')

def contact(request):
    return render(request, 'home/contactus.html')

