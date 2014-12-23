from django.test import TestCase
from django.core.urlresolvers import reverse
from customers.tests.factories import CustomerFactory


class TestAddCustomer(TestCase):
    view_name = 'customer_form_view'

    def test_add_new_customer(self):
        url = reverse(self.view_name)
        response = self.client.post(url, CustomerFactory.attributes())
        self.assertEqual(response.status_code, 302)

    def test_view_form(self):
        url = reverse(self.view_name)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
