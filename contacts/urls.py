from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import ContactList, ContactCreate, ContactDetail


urlpatterns = [
    url(r'^contact/$', ContactList.as_view(), name='contact_list'),
    url(r'^contact/create/$', ContactCreate.as_view(), name='contact_create'),
    url(r'^contact/(?P<pk>\d+)/$', ContactDetail.as_view(), name='contact_detail'),
]

