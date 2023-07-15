from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.
# first page
def firstpage(request):
    book = {'title':"dad" , 'price' : 50}
    return render(request,"firstpage.html" , {'book':book})


def webpage(request):
    return render(request,"webpage.html")

#view of colorpicker
def colorpicker(request):
    return render(request,'colorpicker.html')


def clock(request):
    return render(request,'clock.html')

def calculator(request):
    return render(request , 'calculator.html')

def tool(request):
    return render(request,'tool.html')

def slides(request):
    return render(request,'slides.html')
def rgb(request):
    return render(request,'rgb.html')
def rgba(request):
    return render(request,'rgba.html')
