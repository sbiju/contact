from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView
from django.core.urlresolvers import reverse_lazy, reverse
from .models import Contact
# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"


class ContactList(ListView):
    model = Contact
    queryset = Contact.objects.all().order_by('first_name')
    paginate_by = 8


class ContactCreate(CreateView):
    model = Contact
    fields = ['first_name', 'last_name', 'phone', 'email', 'house', 'street', 'city', 'state', 'photo']
    success_url = reverse_lazy('contact_list')


class ContactDetail(DetailView):
    model = Contact
    queryset = Contact.objects.all()