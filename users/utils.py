from django.db.models import Count

from .models import *


class DataMixim:
    def get_user_context_data(self, **kwargs):
        context = kwargs

        cat_employee = CategoryEmployee.objects.annotate(profiles_count=Count('profile'))
        context['cat_employee'] = cat_employee

        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
