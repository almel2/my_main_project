from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('book-list/', views.BookList.as_view(), name='book_list'),
]