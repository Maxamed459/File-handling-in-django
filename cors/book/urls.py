from django.urls import path
from .models import Book
from . import views

urlpatterns = [
    path("upload-book", views.book_view, name="book"),
    path("list/", views.list, name="list"),
    path("delete/<int:pk>/", views.delete_book, name="delete-book"),
]