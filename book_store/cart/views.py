from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from celery_tasks.tasks import data_synchronization, test_celery
from store.models import Book

from .cart import Cart
from .forms import CartAddBookForm


@require_POST
def cart_add(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    form = CartAddBookForm(request.POST)
    if form.is_valid():
        c_data = form.cleaned_data
        cart.add(book=book,
                 quantity=c_data['quantity'],
                 update_quantity=c_data['update'])
    return redirect('cart_detail')


def cart_remove(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    cart.remove(book)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})


def session_test(request):
    data_synchronization.delay()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits
    request.session['num_visits'] += 1
    context = {
        'num_visits': num_visits,
    }
    return render(request, 'cart/visits.html', context=context)
