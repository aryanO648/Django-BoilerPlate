from django.urls import path
from .views import UserCreateView, UserListView, UserDetailView, \
    BookCreateView, BookListView, BookDetailView, \
    BorrowedBooksCreateView, BorrowedBooksListView, BorrowedBooksDetailView,BookUpdateView

urlpatterns = [
    # User URLs
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    # Book URLs
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),


    # BorrowedBooks URLs
    path('borrowedbooks/create/', BorrowedBooksCreateView.as_view(), name='borrowedbooks-create'),
    path('borrowedbooks/', BorrowedBooksListView.as_view(), name='borrowedbooks-list'),
    path('borrowedbooks/<int:pk>/', BorrowedBooksDetailView.as_view(), name='borrowedbooks-detail'),
]
