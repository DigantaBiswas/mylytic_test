from django.views.generic.edit import DeleteView

from core_management.models import Order


class OrderDeleteView(DeleteView):
    model = Order
    success_url = "/product-list"

    def get_template_names(self):
        return ['base/delete_confirmation.html']
