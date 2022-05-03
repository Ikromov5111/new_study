from django.urls import path
from .views import TodoListApiView,TodoDetailApiView

urlpatterns = [
    path("todolist/",TodoListApiView.as_view()),
    path("todolist/<int:pk>",TodoDetailApiView.as_view()),
]