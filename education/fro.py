from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='Home'),
    path('about', about, name='About'),
    path('products', pro, name='Product'),
    path('Api', api, name='Apis'),
    path('contact', con, name='Contact'),
]
