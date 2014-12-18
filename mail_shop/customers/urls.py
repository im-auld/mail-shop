from django.conf.urls import patterns, url


customers_patterns = patterns(
    'customer.views',
    url(r'^customers/', 'index')
)
