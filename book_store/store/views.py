from cart.forms import CartAddBookForm

from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from store.models import Book


def index(request):
    return render(request, 'store/index.html', {})


class BookList(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'store/book_list.html'


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    cart_form = CartAddBookForm()
    context = {
        'book': book,
        'cart_form': cart_form,
    }
    return render(request, 'store/book_detail.html', context=context)
