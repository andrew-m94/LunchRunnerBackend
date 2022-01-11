from django.urls import path
from orders import views

urlpatterns = [
    path('', views.user_orders),
    path('all/', views.get_all_orders),
    path('order/<int:pk>/', views.update_status),
]