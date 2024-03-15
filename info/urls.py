from django.urls import path

from .views import *

urlpatterns = [
    path('', InfoPage.as_view(), name='home_info'),
]
