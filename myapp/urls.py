
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),             # Product listing with search
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),  # Product detail with recommendations
]
