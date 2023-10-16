from django.shortcuts import render

from book.models import *


# Create your views here.


def get_book(request):
    query = Book.objects.all()
    return render(request, "books/books.html", {"render_book": query})

def book_details(request , book_id):
    query = Book.objects.get(id=book_id)
    return render(request, "books/book_details.html", {"book": query})
