from django.conf.urls import patterns, url


customers_patterns = patterns(
    'customers.views',
    url(r'^customers/', 'index', name='index'),
    url(
        r'^customer/(?P<customer_id>\d+)/',
        'customer_view',
        name='customer_view'
    ),
    url(
        r'^customer/add$',
        'add_customer',
        name='customer_form_view'
    ),
)
