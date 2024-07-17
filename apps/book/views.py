from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from apps.core.constance import BOOK_CATEGORY, BOOK_FORMAT
from . import utils
from . import models
from .forms import PostBookForm

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

# def book_post(request):
#     # breakpoint()
#     return render(request, 'post.html')

def book_post(request):
    # breakpoint()
    if request.method == 'GET':
        form = PostBookForm()
        return render (request, 'book_post.html', {"form": form})
    elif request.method == 'POST':
        data = request.POST
        form = PostBookForm(data)

        if form.is_valid():
            data = form.cleaned_data
            books = models.Book(
                isbn= data.get('isbn'),
                title= data.get('title'),
                description= data.get('description'),
                page_count= data.get('pages'),
                category= data.get('category'),
                published_date= data.get('published_date'),
                publisher= data.get('publisher'),
                lang= data.get('lang'),
                edition= data.get('edition'),
                book_format= data.get('b_format'),
            )
            books.save()
            #breakpoint()
            for i in data.get('tag'):
                us = models.Tag.objects.get(name=i)
                books.tags.add(us.id)
            for i in data.get('author'):
                i = str(i).split(' ')
                at = models.Author.objects.get(first_name = i[0], last_name = i[1])
                authors = models.BookAuthor(
                    book= models.Book.objects.get(isbn=data.get('isbn')),
                    author= at
                )
                authors.save()
            #books.save()
            
            # authors = models.BookAuthor(
            #     book=data.get('isbn'),
            #     author=data.get('author')
            # )
            # authors.save()


            return redirect("myread-urls:home-page")