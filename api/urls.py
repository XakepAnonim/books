from django.urls import path
from .views import *

urlpatterns = [
    path('books', BookViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='book-list'),
    path('books/<int:pk>', BookViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='books'),

    path('books/list', book_list, name='book-list'),
    path('books-detail/<int:pk>', book_detail, name='book-detail'),
    path('books/create', book_create, name='book-create'),
    path('books-update/<int:pk>', book_update, name='book-update'),
    path('books-delete/<int:pk>', book_delete, name='book-delete'),
]
