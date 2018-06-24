from todos.views import ListCreateTodoView
from django.conf.urls import url

urlpatterns = [
    url('/todos', ListCreateTodoView.as_view())
]
