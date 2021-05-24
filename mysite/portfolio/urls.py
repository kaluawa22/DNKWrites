from django.urls import path
from . import views


from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^products/$', views.products, name='products'),
    url(r'^shop/$', views.shop, name='shop'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)