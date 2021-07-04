from django.utils import timezone
from django.views.generic.list import ListView

from core_management.models import Product


class ProductListView(ListView):

    model = Product
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def get_template_names(self):
        return ['core_management/generic_list.html']