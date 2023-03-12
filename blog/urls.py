#contains the urls of our page


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),    #always give clear names: from where to where it is directing Example: we are going to home of blog page
    path('about/', views.about, name='blog-about'), #this means that the requests we have got from urls.py file from project will be directed here
]