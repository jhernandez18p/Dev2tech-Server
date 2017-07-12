from django.conf.urls import url, include
from local_apps.frontend import views as frontend


urlpatterns = [
    url(r'^$', frontend.home, name='inicio'),
    url(r'^contacto$', frontend.contact, name='contacto'),
    url(r'^contacto/error$', frontend.contact_error, name='contacto-error'),
    url(r'^contacto/gracias$', frontend.contact_thanks, name='contacto-gracias'),
    url(r'^contacto/rapido$', frontend.quick_contact, name='contacto-rapido'),
    url(r'^servicios$', frontend.services, name='servicios'),
    url(r'^servicios/(?P<slug>[-\w]+)$', frontend.service_detail, name='servicio-detalle'),
    url(r'^trabajos$', frontend.work, name='trabajos'),
    url(r'^trabajos/(?P<slug>[-\w]+)$', frontend.work, name='trabajo-detalle'),
    url(r'^tecnologias$', frontend.technology, name='tecnologias'),
    url(r'^tecnologias/(?P<slug>[-\w]+)$', frontend.technology, name='tecnologia-detalle'),
]

