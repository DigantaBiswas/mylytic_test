from django.views.generic.edit import UpdateView

from core_management.models import Order


class OrderUpdateView(UpdateView):
    model = Order
    fields = ['customer_name', 'customer_phone', 'customer_email', 'product', 'quanity']

    def get_template_names(self):
        return ['core_management/generic_update.html']
