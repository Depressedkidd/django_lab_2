from django.urls import path
from book.views import *
from . import views

urlpatterns = [
    path('', get_book),
    path('<int:book_id>', views.book_details, name='book'),
]
