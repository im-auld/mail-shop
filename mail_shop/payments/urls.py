from django.conf.urls import patterns, url


payments_patterns = patterns(
    'payments.views',
    url(
        r'^payments/(?P<mailbox_id>\d+)$',
        'payment_view',
        name='filled_payment_view'
    ),
    url(
        r'^payments$',
        'payment_view',
        name='payment_view'
    )
)
