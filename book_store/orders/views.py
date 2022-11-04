from cart.cart import Cart

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


from .forms import OrderForm
from .models import Order, OrderBook


class CreateOrder(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders/create_order.html'
    success_url = reverse_lazy('cart_detail')

    def form_valid(self, form):
        cart = Cart(self.request)
        order = form.save()
        for item in cart:
            OrderBook.objects.create(order=order,
                                     book=item['book'],
                                     price=item['price'],
                                     quantity=item['quantity'])
        cart.clear()
        return super(CreateOrder, self).form_valid(form)


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderBook.objects.create(order=order,
                                         book=item['book'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return render(request, 'orders/success_order.html',
                          {'order': order})
    else:
        form = OrderForm()
    return render(request, 'orders/create_order.html',
                  {'cart': cart, 'form': form})
