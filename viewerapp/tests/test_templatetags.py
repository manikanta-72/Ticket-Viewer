from django.test import SimpleTestCase
from viewerapp.templatetags.custom_tags import date_time

class TestTags(SimpleTestCase):

    def test_data_time(self):
        test_input = '2021-11-25T00:36:03Z'
        self.assertEquals(date_time(test_input),'2021-11-25 00:36:03')
