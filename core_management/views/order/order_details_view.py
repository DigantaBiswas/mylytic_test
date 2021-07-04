from django.shortcuts import render
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from core_management.models import Order, Cart


class OrderDetailView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(OrderDetailView, self).dispatch(request, *args, **kwargs)

    def get(self, request, **kwargs):
        pk = kwargs.get('pk')
        order = Order.objects.filter(id=pk).last()
        carts = Cart.objects.filter(order_id=order.id)

        context = {
            'order': order,
            'carts': carts,
        }
        return render(request, 'core_management/order_detail.html', context)
