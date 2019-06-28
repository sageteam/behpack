from django.urls import path, re_path
from django.urls import reverse_lazy, reverse

from . import views

app_name = 'panel'
urlpatterns = [
    re_path(r'^$', views.PanelView.as_view(), name='index'),
]


# re_path(r'^registration/$', views.UserFormView.as_view(), name='registration')