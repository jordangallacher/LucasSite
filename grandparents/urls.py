from django.urls import path

from . import views

urlpatterns = [
    path('', views.allgrandparents,name='allgrandparents'),
    path('<int:grandparents_id>/', views.detail6, name='detail6'),
]