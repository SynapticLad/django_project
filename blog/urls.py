#contains the urls of our page


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
]