from django.contrib import admin

from .models import Order, OrderBook


class OrderBookInline(admin.TabularInline):
    model = OrderBook
    raw_id_fields = ['book', ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'city', 'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderBookInline]
