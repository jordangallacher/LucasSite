from django.urls import path

from . import views

urlpatterns = [
    path('', views.allmoments,name='allmoments'),
    path('<int:specialmoments_id>/', views.detail2, name='detail2'),
]