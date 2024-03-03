from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('clients/', clients, name='clients'),
    path('clientregister/', clientregister, name='clientregister'),
    path('clientservice/', service, name='clientservice'),
    path('items/', items, name='items'),
    path('qushish/', qushish, name='qushish'),
    path('maxsulotni-topshirish/', clientend, name='clientend'),
    path('organizations/', organizations, name='organizations'),
    path('addorganizations/', addorganizations, name='addorganizations'),
    path('qarzdorliklar/', qarz, name='qarz'),
    path('invoice/', invoice, name='invoice'),
    path('addworker/', addworker, name='addworker'),
    path('workers/', workers, name='workers')
]