from django.urls import path
from . import views

# Django recognizes path urls when there are defined in the variable 'urlpatterns'

app_name = 'myread-urls'
urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('class', views.HomePage.as_view(), name='home-pae-class')
]