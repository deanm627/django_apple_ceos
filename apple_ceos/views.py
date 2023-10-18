from django.shortcuts import render

from .models import CEO

# Create your views here.
from django.views import generic

class CEOListView(generic.ListView):
    model = CEO