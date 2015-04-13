from django.conf.urls import patterns, url


transactions_patterns = patterns(
    'transactions.views',
    url(
        r'^transactions/(?P<mailbox_id>\d+)$',
        'transaction_view',
        name='filled_transaction_view'
    ),
    url(
        r'^transactions$',
        'transaction_view',
        name='transaction_view'
    )
)
