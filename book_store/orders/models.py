from django.db import models
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    first_name = models.CharField(_('first name'), max_length=50)
    last_name = models.CharField(_('last name'), max_length=50)
    email = models.EmailField()
    address = models.CharField(_('address'), max_length=250)
    city = models.CharField(_('city'), max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')
        ordering = ('-created', )

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.orderbook_set.all())


class OrderBook(models.Model):
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    book = models.ForeignKey('store.Book', on_delete=models.CASCADE)
    price = models.DecimalField(_('price'), max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(_('quantity'), default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
