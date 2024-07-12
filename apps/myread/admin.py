from django.contrib import admin
from .models import MyRead, StatusPercent

# Register your models here.

# class MyReadStack(admin.StackedInline):
#     model = StatusPercent
#     readonly_fields = ('percentage_read_range', 'read_status')
#     extar = 1

class MyReadAdmin(admin.ModelAdmin):
    list_display = ('reader_username', 'book_isbn', 'percentage_read', 'start_read_date', 'end_read_date')
    search_fields = ('book_isbn', 'reader_username', 'percentage_read') 
    list_filter = ('book_isbn', 'reader_username', 'percentage_read')

admin.site.register(MyRead, MyReadAdmin)
admin.site.register(StatusPercent)