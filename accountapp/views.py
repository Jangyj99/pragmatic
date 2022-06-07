from django.http import HttpResponse
from django.shortcuts import render

# Create your views here. 원하는 뷰 만들기

def hello_world(request):
    return render(request, 'accountapp/hello_world.html')