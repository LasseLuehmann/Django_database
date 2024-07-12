from django.contrib import admin
from .models import Book, Author, BookAuthor, Tag

# Register your models here.

class BookAuthorInline(admin.StackedInline):
    model = BookAuthor
    extra = 1

class BookAdmin(admin.ModelAdmin):
    inlines = (BookAuthorInline,)
    list_display = ('isbn', 'title', 'publisher', 'published_date', 'lang', 'book_format')
    search_fields = ('title', 'isbn', 'publisher', 'published_date')
    list_filter = ('category', 'book_format', 'published_date', 'lang')

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(BookAuthor)
admin.site.register(Tag)
