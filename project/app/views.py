from django.shortcuts import render
from .models import Book
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
# Create your views here.

class BookListView(ListView):
    model = Book
    template_name = 'index.html'
    context_object_name = 'books'

class BookCreateView(CreateView):
    model = Book
    template_name = 'form.html'
    fields = '__all__'
    success_url = reverse_lazy('index')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'delete.html'
    success_url = reverse_lazy('index')

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'form.html'
    fields = '__all__'
    success_url = reverse_lazy('index')

class BookDetailView(DetailView):
    model = Book
    template_name = 'detail.html'
    context_object_name = 'book'

