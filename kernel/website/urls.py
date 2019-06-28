from django.urls import path, re_path

from .views import HomeView
from .views import AboutView
from .views import ContactView
from .views import ProductView
from .views import ProductDetailView
from .views import SlovakiProductDetailView
from .views import BlogView
from .views import BlogDetailView
from .views import SlovakiBlogDetailView
from .views import AwardsView


app_name = 'website'
urlpatterns = [
    re_path(r'^$', HomeView.as_view(), name='home'),
    re_path(r'^/$', HomeView.as_view(), name='home'),
    re_path(r'^home/$', HomeView.as_view(), name='home'),
    re_path(r'^index/$', HomeView.as_view(), name='home'),
    re_path(r'^about/$', AboutView.as_view(), name='about'),
    re_path(r'^contact/$', ContactView.as_view(), name='contact'),
    re_path(r'^awards/$', AwardsView.as_view(), name='awards'),
    re_path(r'^products/$', ProductView.as_view(), name='products'),
    re_path(r'^product/(?P<sku>[A-Za-z0-9\-\_]+)/(?P<pk>\d+)$', ProductDetailView.as_view(), name='product'),
    re_path(r'^product/(?P<sku>[A-Za-z0-9\-\_]+)/sk/(?P<pk>\d+)$', SlovakiProductDetailView.as_view(), name='slovakiproduct'),
    re_path(r'^news/$', BlogView.as_view(), name='news'),
    re_path(r'^news/(?P<sku>[A-Za-z0-9\-\_]+)/(?P<pk>\d+)$', BlogDetailView.as_view(), name='post'),
    re_path(r'^news/(?P<sku>[A-Za-z0-9\-\_]+)/sk/(?P<pk>\d+)$', SlovakiBlogDetailView.as_view(), name='slovakipost'),
    
]
