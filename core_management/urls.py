from django.urls import path

from core_management.views import CategoryCreateView, ProductUpdateView
from core_management.views.order.order_create_view import OrderCreateView
from core_management.views.order.order_delete_view import OrderDeleteView
from core_management.views.order.order_details_view import OrderDetailView
from core_management.views.order.order_list_view import OrderListView
from core_management.views.order.order_update_view import OrderUpdateView
from core_management.views.product.product_create_view import ProductCreateView
from core_management.views.product.product_delete_view import ProductDeleteView
from core_management.views.product.product_list_view import ProductListView

urlpatterns = [
    path('product-list', ProductListView.as_view(), name='product-list'),
    path('product-create', ProductCreateView.as_view(), name='product-create'),
    path('product-edit/<pk>', ProductUpdateView.as_view(), name='product-edit'),
    path('product-delete/<pk>/', ProductDeleteView.as_view(), name='product-delete'),
    path('category-create', CategoryCreateView.as_view(), name='category-create'),

    path('order-list', OrderListView.as_view(), name='order-list'),
    path('', OrderCreateView.as_view(), name='order-create'),
    path('order-edit', OrderUpdateView.as_view(), name='order-edit'),
    path('order-delete/<pk>/', OrderDeleteView.as_view(), name='order-delete'),
    path('order-detail/<pk>/', OrderDetailView.as_view(), name='order-detail')

]
