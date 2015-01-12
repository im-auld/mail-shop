from django.conf.urls import patterns, url


payments_patterns = patterns(
    'payments.views',
    url(
        r'^payments$',
        'payment_view',
        name='payment_view'
    )
)
