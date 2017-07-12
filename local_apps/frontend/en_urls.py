from django.conf.urls import url, include
from local_apps.frontend import views as frontend


urlpatterns = [
    url(r'^$', frontend.home, name='home'),
    url(r'^contact$', frontend.contact, name='contact'),
    url(r'^contact/error$', frontend.contact_error, name='thanks-error'),
    url(r'^contact/quick$', frontend.quick_contact, name='quick-contact'),
    url(r'^contact/thanks$', frontend.contact_thanks, name='thanks-contact'),
    url(r'^services$', frontend.services, name='services'),
    url(r'^services/(?P<slug>[-\w]+)$', frontend.service_detail, name='service-detail'),
    url(r'^technologies$', frontend.technology, name='technologies'),
    url(r'^technologies/(?P<slug>[-\w]+)$', frontend.technology, name='technology-detail'),
    url(r'^works$', frontend.work, name='works'),
    url(r'^works/(?P<slug>[-\w]+)$', frontend.work, name='work-detail'),
]

