from django.test import TestCase
from django.core.urlresolvers import reverse
from customers.tests.factories import CustomerFactory


class CustomerFixtureMixin(object):
    def setUp(self):
        self.customer = CustomerFactory()
        self.customer.save()


class TestCustomerView(CustomerFixtureMixin, TestCase):
    view_name = 'customer_view'

    def test_invalid_customer_id(self):
        url = reverse(self.view_name, kwargs={'customer_id': 0})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_valid_customer_id(self):
        url = reverse(
            self.view_name,
            kwargs={
                'customer_id': self.customer.pk,
            }
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
