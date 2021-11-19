from django.test import TestCase

# Create your tests here.

from django.test import Client
from todo.models import assignment

class test_todo(TestCase):
    def setUp(self):
        self.client = Client()
        self.assign = assignment.objects.create(breakfast=False, task="Try")
        self.assign2 = assignment.objects.create(breakfast=True, task="Try")
    def test_page(self):
        a=self.client.get('/liste/0/')
        self.assertContains(a, "Add")
        b=self.client.get('/liste/1/')
        self.assertContains(b, "Add")
    def test_page_14(self):
        for i in range(0,13):
            a=assignment.objects.create(breakfast=False, task="Try")
        for j in range(0,6):
            b=assignment.objects.create(breakfast=True, task="Try")
        c=self.client.get('/liste/0/')
        d=self.client.get('/liste/1/')
        self.assertContains(c, "Go to breakfast page")
        self.assertContains(d, "Go to table")
