from django.shortcuts import render
from django.views.generic import ListView

from store.models import Book

def index(request):
    return render(request, 'store/index.html', {})



class BookList(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'store/book_list.html'
