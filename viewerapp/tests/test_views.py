


from django.test import client
from django.test.testcases import TestCase, Client
from django.urls import reverse
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.ticket_by_id_url = reverse('ticket_by_id', args=[1])

    def test_index_Get(self):
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'index.html')

    def test_ticket_by_id_Get(self):
        response = self.client.get(self.ticket_by_id_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'ticket_by_id.html')

    
