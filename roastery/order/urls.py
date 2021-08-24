from django.urls import path
from rest_framework.authtoken import views

from .views import checkout, OrdersList

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('checkout/', checkout), 
    path('orders/', OrdersList.as_view()), 
]