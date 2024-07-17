from django.shortcuts import render
from django.http import HttpResponse

from apps.core.constance import BOOK_CATEGORY, BOOK_FORMAT
from . import utils
from . import models

# Create your views here.

def book_detail(request, isbn):
    book = models.Book.objects.get(pk=isbn)

    # for item in book.category:
    #     item = BOOK_CATEGORY[item]
    # for item in book.book_format:
    #     item = BOOK_FORMAT[item]

    # book.category = BOOK_CATEGORY.get(book.category)
    # book.book_format = BOOK_FORMAT.get(book.book_format)

    context = {
        'book': book
    }
    return render(request, 'book_detail.html', context=context)