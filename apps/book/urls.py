from django.urls import path
from . import views


app_name = 'book-urls'
urlpatterns = [
    path('book/<isbn>', views.book_detail, name='book-detail'),
    
]