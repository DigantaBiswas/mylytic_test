from django.utils import timezone
from django.views.generic.list import ListView

from core_management.models import Order


class OrderListView(ListView):

    model = Order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def get_template_names(self):
        return ['core_management/order_list.html']