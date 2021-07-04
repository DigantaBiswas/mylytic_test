from django.views.generic.edit import DeleteView

from core_management.models import Product


class ProductDeleteView(DeleteView):
    model = Product
    success_url = "/product-list"

    def get_template_names(self):
        return ['base/delete_confirmation.html']
