from warehouse_api.models import Book
from .serializers import BookSerializer

from rest_framework import viewsets

from django.shortcuts import render


def index(request):
    return render(request, 'warehouse_api/index.html', {})


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
