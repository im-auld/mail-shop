from django.conf.urls import patterns, url


mailboxes_patterns = patterns(
    'mailboxes.views',
    url(
        r'^mailboxes/$',
        'index',
        name='mailboxes_index'
    ),
    url(
        r'^mailboxes/(?P<mailbox_id>\d+)/',
        'mailbox_view',
        name='mailbox_view'
    ),
)
