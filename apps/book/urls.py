from django.urls import path
from . import views


app_name = 'book-urls'
urlpatterns = [
    path('book/<isbn>', views.book_detail, name='book-detail'),
    path('book/post/', views.book_post, name='book-post'), # the http method 'POST' usually don't work without an ending '/'
]