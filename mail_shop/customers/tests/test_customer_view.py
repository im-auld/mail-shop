from django.test import TestCase
from django.core.urlresolvers import reverse


class TestCustomerView(TestCase):
    view_name = 'customer_view'

    def test_invalid_customer_id(self):
        url = reverse(self.view_name, kwargs={'customer_id': 9999999999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
