from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^payment/$', views.payment_process, name='payment'),
    url(r'^done/$', views.payment_done, name='done'),
    url(r'^cancelled/$', views.payment_cancelled, name='cancelled'),
]
