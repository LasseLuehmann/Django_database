# Generated by Django 5.0.6 on 2024-07-04 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_book_authors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='book', through='book.BookAuthor', to='book.author'),
        ),
    ]
