from django.test import SimpleTestCase
from django.urls import reverse, resolve
from viewerapp.views import index, ticket_by_id

class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_ticket_by_id_url_is_resolved(self):
        url = reverse('ticket_by_id', args=[1])
        self.assertEquals(resolve(url).func, ticket_by_id)
