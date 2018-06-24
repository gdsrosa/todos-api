from todos.models import Todo
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    done = serializers.BooleanField(default=False)

    model = Todo
    fields = ('title', 'body', 'done')
