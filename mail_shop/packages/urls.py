from django.conf.urls import patterns, url


packages_patterns = patterns(
    'packages.views',
    url(
        r'^packages/$',
        'index',
        name='index'
    ),
    url(
        r'^package/(?P<package_id>\d+)/',
        'package_view',
        name='package_view'
    ),
)
