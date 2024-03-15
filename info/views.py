from django.views.generic import ListView
from django.db.models import Sum

from .models import *
from users.models import Profile


class InfoPage(ListView):
    model = Info
    template_name = 'info/home_info.html'
    context_object_name = 'chart_info'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        info_aggregate = Profile.objects.aggregate(
            total_collected=Sum('collected'),
            total_transported=Sum('transported'),
            total_discharge=Sum('discharge'),
            total_shipment=Sum('shipment'),
            total_others=Sum('others')
        )
        context.update(info_aggregate)
        return context
