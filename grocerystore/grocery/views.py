from django.shortcuts import render
from django.http import HttpResponse
from .models import Grocery
# Create your views here.

def home(request):
    search = request.GET.get("searchgrocery")
    if search:
        grocery = Grocery.objects.filter(name__icontains=search)
    else:
        grocery = Grocery.objects.all()
    return render(request, "home.html", {"search": search, "grocery": grocery})