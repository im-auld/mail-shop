import random

import factory
from customers.models import Customer
from customers.models import STATES


class CustomerFactory(factory.Factory):
    class Meta:
        model = Customer

    f_name = factory.Sequence(lambda n: 'First{}'.format(n))
    l_name = factory.Sequence(lambda n: 'Last{}'.format(n))
    line_1 = factory.Sequence(lambda n: '{} Test Street')
    line_2 = 'Apt 3'
    city = 'Test City'
    state = random.choice(STATES)[0]
    zip_code = '12345'
    email = factory.Sequence(lambda n: 'testcustomer{}@test.com'.format(n))


    @factory.sequence
    def phone_num(n):
        a = n // 10000
        b = n % 10000
        return '%03d-555-%04d' % (a, b)
