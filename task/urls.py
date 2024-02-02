from django.urls import path
from .views import *

urlpatterns = [
  path('', TaskListView.as_view(), name='home'),
  path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
  path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
  path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
  path('task/new/', TaskCreateView.as_view(), name='task_new')
]