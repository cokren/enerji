from django.shortcuts import render,HttpResponse
import time

# Create your views here.
def index(request):

    return render(request,"index.html",)