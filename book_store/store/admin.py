from django.contrib import admin

from store.models import Book, Author, Publisher, Category

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'isbn', 'code',
                    'publisher', 'category', 'str',
                    'year', 'language', 'image', 'price',
                    'description']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name',]


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name',]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]
