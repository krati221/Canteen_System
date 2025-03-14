"""canteen_ordering_sys URL Configuration
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('order.urls')),
]
