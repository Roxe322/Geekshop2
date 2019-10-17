import debug_toolbar
from django.conf.urls import include
from django.contrib import admin
import mainapp.views as mainapp

from django.conf import settings
from django.conf.urls.static import static

from django.urls import re_path

urlpatterns = [
    re_path(r'^$', mainapp.main, name='main'),
    re_path(r'^products/', include('mainapp.urls', namespace='products')),
    re_path(r'^contact/', mainapp.contact, name='contact'),
    re_path(r'^auth/verify/google/oauth2/', include("social_django.urls", namespace="social")),
    re_path(r'^auth/', include('authapp.urls', namespace='auth')),
    re_path(r'^basket/', include('basketapp.urls', namespace='basket')),

    re_path(r'^order/', include('ordersapp.urls', namespace='order')),

    re_path(r'^admin/', include('adminapp.urls', namespace='admin')),
]

if settings.DEBUG:
    urlpatterns += [re_path('^__debug__/$', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
