from django.test import TestCase
from todos.models import Todo

#Model Test
class TodoTest(TestCase):
    
    def create_todo(self, title='Go to workshop', body='Learn with Python Workshop', done=False):
        return Todo.objects.create(title=title, body=body, done=done)
    
    def test_create_todo(self):
        todo = self.create_todo()
        self.assertTrue(isinstance(todo, Todo))
        self.assertEqual(todo.title, 'Go to workshop')
