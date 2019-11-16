from django.shortcuts import render
from .models import Seed, Answer

# Create your views here.
def index(request):
    return render(request,'index.html')

def hey(request):

    return render(request,'hey.html')