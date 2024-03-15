from django.urls import path
from .views import *

urlpatterns = [
    path('', ProfileInfo.as_view(), name='profiles'),

    path('category_employee/<slug:category_slug>', ProfileCategory.as_view(), name='category_employee'),
    path('show_profile/<slug:show_user_slug>/', ShowProfile.as_view(), name='show_profile'),
]