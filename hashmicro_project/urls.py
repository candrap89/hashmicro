from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('uninstall/', views.uninstall, name='uninstall'),
    path('product', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('create/', views.product_create, name='product_create'),
    path('<int:pk>/update/', views.product_update, name='product_update'),
    path('<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('bulk-delete/', views.product_bulk_delete, name='product_bulk_delete'),
]