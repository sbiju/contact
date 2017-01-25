from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView
from django.core.urlresolvers import reverse_lazy, reverse
from .models import Contact
# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"


class ContactList(ListView):
    model = Contact


class ContactCreate(CreateView):
    model = Contact
    fields = ['first_name', 'last_name', 'phone', 'email', 'house', 'street', 'city', 'state']
    success_url = reverse_lazy('contact_list')