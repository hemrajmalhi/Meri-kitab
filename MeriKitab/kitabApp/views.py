from django.shortcuts import render
from .models import SellBook1
from .forms import SellBookForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404


# Create your views here.


def home(request):
    buyBookHome = SellBook1.objects.all().order_by('-id')[:6]

    context = {'buyBook': buyBookHome}
    return render(request, "merikitab/home.html", context)


def about(request):
    return render(request, "merikitab/about.html")


def contact(request):
    return render(request, "merikitab/contact.html")


def buybook(request):
    buBook = SellBook1.objects.all().order_by('-id')
    context = {"buybook": buBook}
    return render(request, "books/buybook.html", context)


def sellbook(request):
    message = "Your data has been submitted successfully."
    if request.method == 'POST':
        form = SellBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'books/sellbook.html', {"message": message})
    else:
        form = SellBookForm()
    return render(request, 'books/sellbook.html', {'form': form})


def bookDetail(request, pk):
    bookDetails = get_object_or_404(SellBook1, pk=pk)
    category_mapping = {
        1: "Fiction",
        2: "Non Fiction",
        3: "Children's Book",
    }
    category_id = bookDetails.category
    category_name = bookDetails.category
    category_name = category_mapping.get(category_id)
    print(f"Provided category_id: {category_id}")
    print(f"Category mapping: {category_mapping}")
    print(f"Resolved category_name: {category_name}")
    context = {'bookDetail': bookDetails, 'category_name': category_name}
    return render(request, "books/bookdetail.html", context)
