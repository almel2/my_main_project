from .models import Book

from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'author', 'code',
                  'publisher', 'category',
                  'quantity_str', 'year',
                  'language', 'image', 'price',
                  'description', 'quantity']