from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
# Create your views here.

class TaskListView(ListView):
  model = Task
  template_name = 'task/home.html'


class TaskDetailView(DetailView):
  model = Task
  template_name = 'task/task_detail.html' 


class TaskCreateView(CreateView):
  model = Task
  fields = ['title', 'description', 'deadline']
  template_name = 'task/task_new.html'


class TaskUpdateView(UpdateView):
  model = Task
  fields = ['title', 'description', 'deadline']
  template_name = 'task/task_update.html'

class TaskDeleteView(DeleteView):
  model = Task
  template_name = 'task/task_delete.html'
  success_url  = reverse_lazy('home')