from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookForm
from .models import Book


def book_view(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        message = "Invalid data"
        return render(request, "book/index.html", {"form": BookForm,  "message": message})
    return render(request, "book/index.html", {"form": BookForm})

def list(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "book/list.html", context)

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect("list")