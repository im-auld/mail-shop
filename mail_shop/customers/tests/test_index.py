from django.test import TestCase
from django.core.urlresolvers import reverse


class TestIndex(TestCase):
    view_name = 'index'

    def test_index(self):
        url = reverse(self.view_name)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
