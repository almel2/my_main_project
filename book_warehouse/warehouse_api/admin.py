from django.contrib import admin

from warehouse_api.models import Book, BookInstance


class BookInline(admin.TabularInline):
    model = BookInstance
    raw_id_fields = ['book']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code',
                    'publisher', 'quantity_str',
                    'year', 'language', 'image', 'price',
                    'description']
    inlines = [BookInline]
