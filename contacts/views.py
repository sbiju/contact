from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView
from django.core.urlresolvers import reverse_lazy, reverse
from .models import Contact
from django.shortcuts import render, get_object_or_404, redirect
from .mixins import LoginRequiredMixin
from django.conf import settings

user=settings.AUTH_USER_MODEL


class HomePageView(TemplateView):
    template_name = "home.html"


class ContactList(LoginRequiredMixin, ListView):
    model = Contact
    paginate_by = 8

    def get_queryset(self):
        return Contact.objects.all().order_by('first_name')


class ContactCreate(LoginRequiredMixin, CreateView):
    model = Contact
    fields = ['first_name', 'last_name', 'phone', 'email', 'house', 'street', 'city', 'state', 'photo']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(ContactCreate, self).form_valid(form)


class ContactUpdate(LoginRequiredMixin, UpdateView):
    model = Contact
    fields = ['first_name', 'last_name', 'phone', 'email', 'house', 'street', 'city', 'state', 'photo']


class ContactDetail(LoginRequiredMixin, DetailView):
    model = Contact
    queryset = Contact.objects.all()


class ContactDelete(LoginRequiredMixin, DeleteView):
    model = Contact
    success_url = reverse_lazy('contact_list')