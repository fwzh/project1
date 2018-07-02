from django.shortcuts import render,HttpResponse

# Create your views here.

from django.shortcuts import render

def page_errors(request):
    return render(request, '500.html')

def show(request):
        return render(request,'index.html');
