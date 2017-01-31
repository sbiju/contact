from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from .mixins import LoginRequiredMixin
from .models import Contact, Meeting


# class MeetingList(LoginRequiredMixin, ListView):
#     model = Meeting
#     # queryset= Meeting.objects.all()
#     paginate_by = 5
#
#     def get_queryset(self):
#         return self.model.objects.filter(user=self.request.user).order_by('-id')



@login_required
def meeting_list(request):
    queryset_list = Meeting.objects.all()
    # paginator = Paginator(queryset_list, 8)
    # page_request_var = "page"
    # page = request.GET.get(page_request_var)
    # try:
    #     queryset = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     queryset = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset_list,
        "title": "List",

    }
    return render(request, "contacts/meeting_list.html", context)


class MeetingDetail(LoginRequiredMixin, DetailView):
    model = Meeting
    queryset = Meeting.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(MeetingDetail, self).get_context_data(*args, **kwargs)
        # print self.get_object().contact.all()
        # print context
        return context


class MeetingCreate(LoginRequiredMixin, CreateView):
    model = Meeting
    fields = ['title', 'participant', 'notes', 'meeting_date']
    template_name = 'contacts/contact_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(MeetingCreate, self).form_valid(form)


class MeetingUpdate(LoginRequiredMixin, UpdateView):
    model = Meeting
    fields = ['title', 'participant', 'notes', 'meeting_date']
    template_name = 'contacts/contact_form.html'


class MeetingDelete(LoginRequiredMixin, DeleteView):
    model = Meeting
    success_url = reverse_lazy('meeting_list')
    template_name = 'contacts/contact_confirm_delete.html'


class HomePageView(TemplateView):
    template_name = "home.html"


# class ContactList(LoginRequiredMixin, ListView):
#     model = Contact
#     queryset= Contact.objects.all()
#     paginate_by = 5

    # def get_queryset(self):
    #     return self.model.objects.filter(user=self.request.user).order_by('first_name')


def contact_list(request):
    queryset_list = Contact.objects.all()
    paginator = Paginator(queryset_list, 8)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
        "title": "List",
        "page_request_var": page_request_var,
    }
    return render(request, "contacts/contact_list.html", context)


class ContactCreate(LoginRequiredMixin, CreateView):
    model = Contact
    fields = ['first_name', 'last_name', 'job_title', 'email', 'company', 'notes']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(ContactCreate, self).form_valid(form)


class ContactUpdate(LoginRequiredMixin, UpdateView):
    model = Contact
    fields = ['first_name', 'last_name', 'job_title', 'email', 'company', 'notes']


class ContactDetail(LoginRequiredMixin, DetailView):
    model = Contact
    queryset = Contact.objects.all()


class ContactDelete(LoginRequiredMixin, DeleteView):
    model = Contact
    success_url = reverse_lazy('contact_list')