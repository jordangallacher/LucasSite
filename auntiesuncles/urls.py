from django.urls import path

from . import views

urlpatterns = [
    path('', views.allauntiesuncles,name='allauntiesuncles'),
    path('<int:auntiesuncles_id>/', views.detail5, name='detail5'),
]