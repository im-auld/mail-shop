from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mail_shop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

customers_patterns = patterns(
    'customers.views',
    url(r'^customers/', 'index')
)

file_patterns = patterns(
    '',
    (
        r'^customer_photos/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}
    )
)

urlpatterns.extend(customers_patterns)
urlpatterns.extend(file_patterns)
