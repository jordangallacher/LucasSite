from django.urls import path

from . import views

urlpatterns = [
    path('', views.allmummy,name='allmummy'),
    path('<int:mummy_id>/', views.detail3, name='detail3'),
]