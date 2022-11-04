from django.urls import path

from orders import views

urlpatterns = [
    path('', views.CreateOrder.as_view(), name='create_order'),
]
