from django.shortcuts import render
from .models import cloth

# Create your views here.

def index(request):

    cloths = cloth.objects.all()
    
    return render(request, "index.html", {"cloth1" : cloths})