from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from .models import Puppy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class PupListView(ListView):
	model = Puppy
	template_name = 'home.html'

class AddPupView(CreateView):
	model = Puppy
	template_name = 'add_pup.html'
	fields = ['name']
	
class UpdatePuppyView(UpdateView):
	model = Puppy
	template_name = 'change_pup.html'
	fields = ['name']

class DeletePuppyView(DeleteView):
	model = Puppy
	template_name = 'delete_pup'
	success_url = reverse_lazy('home')
	
class DetailPuppyView(DetailView):
	model = Puppy
	template_name = 'detail_pup.html'
