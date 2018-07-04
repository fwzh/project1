from django.shortcuts import render
from django.http import  Http404,HttpResponse


# Create your views here.
def page_not_found(request):
    return render(request,'404.html')

def page_error(request):
    return render(request,'500.html')

def show(request):
    return render(request, 'index.html')
