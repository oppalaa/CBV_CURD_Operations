from django.shortcuts import render
from django.views.generic import ListView,DetailView,UpdateView,CreateView
# Create your views here.
from app.models import *

class School_list(ListView):
    model=School
    context_object_name='ALLSO'
    
class School_detail(DetailView):
    model=School
    context_object_name='sclobj'   
    
    
class School_create(CreateView):
    model=School
    fields='__all__'
    
class School_update(UpdateView):
    model=School
    fields='__all__'

