from django.contrib import admin

from store.models import Author, Book, Category, Publisher


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'code',
                    'publisher', 'category', 'quantity_str',
                    'year', 'language', 'image', 'price',
                    'description']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]
