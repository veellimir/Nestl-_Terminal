from django.views.generic import ListView, DetailView

from .models import *
from .utils import DataMixim


class ProfileInfo(ListView, DataMixim):
    model = Profile
    template_name = 'users/profiles.html'
    context_object_name = 'profiles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_context = self.get_user_context_data(**kwargs)
        context.update(user_context)

        return context


class ProfileCategory(DataMixim, ListView):
    model = Profile
    template_name = 'users/profiles.html'
    context_object_name = 'profiles'

    def get_queryset(self):
        return Profile.objects.filter(employee_category__slug=self.kwargs['category_slug'],
                                      is_public=True).select_related('employee_category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        get_employee = CategoryEmployee.objects.get(slug=self.kwargs['category_slug'])
        c_def = self.get_user_context_data(
            title='Категория - ' + str(get_employee.category_name),
            cat_selected=get_employee.pk
        )
        return dict(list(c_def.items()) + list(context.items()))


class ShowProfile(DataMixim, DetailView):
    model = Profile
    template_name = 'users/show_profile.html'
    slug_url_kwarg = 'user_slug'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context_data(title=context['profile'].name)
        return dict(list(c_def.items()) + list(context.items()))