from django.shortcuts import render
from.models import fooditemsss

# Create your views here.
def index(request):
    f1 = fooditemsss()
    f1.name ='fishfry'
    f1.img = 'no.jfif'
    f1.price = 42
    

    return render(request, "index.html",{'f1':f1})

