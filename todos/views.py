from todos.serializers import TodoSerializer
from todos.models import Todo
from rest_framework import generics

class ListCreateTodoView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()