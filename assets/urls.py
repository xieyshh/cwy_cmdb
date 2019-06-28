from django.urls import path
from assets import views

# app_name = 'assets'

urlpatterns = [
    path('server/', views.server, name='server'),
    path('show/', views.show),
]