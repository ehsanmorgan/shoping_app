from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView,DetailView
from .models import Jewellery,Fashion,Electronic



class Fashion_list(ListView):
	model=Fashion


