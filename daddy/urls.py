from django.urls import path

from . import views

urlpatterns = [
    path('', views.alldaddy,name='alldaddy'),
    path('<int:daddy_id>/', views.detail4, name='detail4'),
]