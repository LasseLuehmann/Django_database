from django import forms
from apps.core.constance import BOOK_CATEGORY, BOOK_FORMAT, LANGUAGES
from apps.book.models import Tag, Author


class PostBookForm(forms.Form):
    isbn = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "isbn-input",
                "placeholder": "Enter isbn"
            }
        )
    )

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "title-input",
                "placeholder": "Enter title"
            }
        )
    )

    pages = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "pages-input",
                "placeholder": "Enter pages"
            }
        )
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "description-input",
                "placeholder": "Enter description"
            }
        )
    )

    category = forms.ChoiceField(
        widget=forms.RadioSelect(
            attrs={
                "class": "form-cat"
            }
        ),
        choices = BOOK_CATEGORY
    )

    author = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                "class": "form-cat"
            }
        )
    )

    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                "class": "form-cat"
            }
        )
    )

    # published_date = forms.DateField(
    #     widget=forms.DateInput(
    #         format=('%Y'),
    #         attrs={
    #             "class": "date-input",
    #             "placeholder": "Enter the year of publishing",
    #             "type": "date"
    #         }
    #     )
    # )

    published_date = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "class": "date-input",
                "placeholder": "Enter the year of publishing"
            }
        )
    )

    publisher = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "publisher-input",
                "placeholder": "Enter the publisher"
            }
        )
    )

    lang = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                "class": "lang-input",
                "placeholder": "Enter the written language"
            }
        ),
        choices=LANGUAGES
    )

    edition = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "edition-input",
                "placeholder": "Enter the edition"
            }
        )
    )

    b_format = forms.ChoiceField(
        widget=forms.RadioSelect(
            attrs={
                "class": "form-cat"
            }
        ),
        choices=BOOK_FORMAT
    )