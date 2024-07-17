from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.db.models import Count

from . import models as mmod
from . import utils
from apps.reader import models as rmod
from apps.book import models as bmod
from apps.core.constance import BOOK_CATEGORY

# Create your views here.

def home_page(request):
    # Return a response
    # View can return valid formats like
    # html, xml, json, etc.
    engaged_reader_cnt = mmod.MyRead.objects.distinct('reader_username').count()
    total_readers_cnt = rmod.Reader.objects.count()
    books_per_category = bmod.Book.objects.values('category').annotate(cnt=Count('*'))

    # for item in books_per_category:
    #     item['category'] = BOOK_CATEGORY.get(item['category'])

    context = {
        'total_readers_cnt': total_readers_cnt,
        'engaged_reader_cnt': engaged_reader_cnt,
        'books_per_category': books_per_category
    }
    return render(request, 'home_page.html', context=context)



class HomePage(TemplateView):
    # TODO: create a new html for this
    template_name = 'home_page.html'
