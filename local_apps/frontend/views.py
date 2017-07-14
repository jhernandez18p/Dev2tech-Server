# -*- coding: utf-8 -*-
from decouple import config
from django.shortcuts import ( get_object_or_404, render, redirect )
from django.views.generic.base import RedirectView
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import ( send_mail, BadHeaderError )
from django.core.urlresolvers import ( reverse_lazy, reverse )
from django.http import ( Http404, HttpResponse, HttpResponseRedirect )

import datetime
import json
import random

from local_apps.frontend.helper import get_lang

class Redirect(RedirectView):
    def get_redirect_url(self):
        lang = 'es'
        url = 'es:inicio'
        context = {}
        
        return reverse_lazy(url)


def lang(request):
    if request.method == "POST":
        if 'url' in request.POST and 'lang_code' in request.POST:
            url = request.POST['url']
            lang_code = request.POST['lang_code']
            lang_ = False
        else:
            url = 'es:inicio'
            lang_code = 'English'
            lang_ = True

        if 'blog' in request.POST:
            blog = request.POST['blog']
            if blog != '':
                url = blog

        print(url)
        render = redirect(url)
        render.set_cookie('lang_code', lang_code)
        render.set_cookie('lang', lang_)
        print(render)
        return render
    
    else:    
        print('La url del post es %s' % url)
        return redirect('es:inicio')

def home(request):
    context = {}
    template = 'frontend/pages/home.html'
    lang = get_lang(request)
    es_url = ''
    en_url = ''

    if str(lang) == 'es':
        pg_title = 'Inicio'
        context['url'] = en_url
    else:
        pg_title = 'Home'
        context['url'] = es_url

    context['lang'] = lang
    context['pg_title'] = pg_title
    context['title'] = en_url
    print(request.LANGUAGE_CODE)
    return render(request,template,context)


def services(request):
    context = {}
    template = 'frontend/pages/services.html'
    lang = get_lang(request)
    es_url = 'servicios'
    en_url = 'services'

    if str(lang) == 'es':
        pg_title = 'Servicios'
        context['url'] = en_url
    else:
        pg_title = 'Services'
        context['url'] = es_url

    context['lang'] = lang
    context['pg_title'] = pg_title
    context['title'] = en_url

    return render(request,template,context)


def service_detail(request,slug=''):
    context = {}
    template = 'frontend/pages/details/service.html'
    lang = get_lang(request)
    es_url = 'servicio-detalle'
    en_url = 'service-detail'

    if str(lang) == 'es':
        pg_title = 'Inicio'
        context['url'] = en_url
    else:
        pg_title = 'Home'
        context['url'] = es_url

    context['lang'] = lang
    context['pg_title'] = pg_title
    context['title'] = "services"

    return render(request,template,context)


def contact(request):
    template = 'frontend/pages/contact.html'
    context = {}
    lang = get_lang(request)
    es_url = 'contacto'
    en_url = 'contact'

    if str(lang) == 'es':
        pg_title = 'Contacto'
        context['url'] = en_url
    else:
        pg_title = 'Contact us'
        context['url'] = es_url

    context['lang'] = lang
    context['pg_title'] = pg_title
    context['title'] = en_url
    return render(request,template,context)


def contact_thanks(request):
    template = 'frontend/widgets/thanks.html'
    context = {}
    lang = get_lang(request)
    es_url = ''
    en_url = ''

    if str(lang) == 'es':
        pg_title = 'Gracias por comunicarse'
        context['url'] = en_url
    else:
        pg_title = 'Thanks for contacting us'
        context['url'] = es_url

    context['lang'] = lang
    context['pg_title'] = pg_title
    return render(request,template,context)


def contact_error(request):
    template = 'frontend/widgets/error.html'
    context = {}
    lang = get_lang(request)
    es_url = ''
    en_url = ''

    if str(lang) == 'es':
        pg_title = 'Error de contacto'
        context['url'] = en_url
    else:
        pg_title = 'Contact Error!'
        context['url'] = es_url

    context['lang'] = lang
    context['pg_title'] = pg_title
    return render(request,template,context)


def quick_contact(request):
    context = {}
    lang = get_lang(request)
    es_url = 'gracias'
    en_url = 'thanks'
    es_error_url = 'error'
    en_error_url = 'error'

    if request.method == "POST":
        if 'name' in request.POST:
            nameForm = request.POST['name']
            print(nameForm)
        if 'phone' in request.POST:
            phoneForm = request.POST['phone']
            print(phoneForm)
        if 'lastname' in request.POST:
            lastnameForm = request.POST['lastname']
            print(lastnameForm)
        if 'email' in request.POST:
            emailForm = request.POST['email']
            print(emailForm)
        if 'message' in request.POST:
            messageForm = request.POST['message']
            print(messageForm)
        if 'action' in request.POST:
            actionForm = request.POST['action']
            print(actionForm)
        if 'business' in request.POST:
            businessForm = request.POST['business']
            print(businessForm)
        if 'country' in request.POST:
            countryForm = request.POST['country']
            print(countryForm)
        
        from_email_user = 'noreply@dev2tech.xyz'
        from_email_main = emailForm
        subject_main = "Mensaje enviado de %s %s" % (nameForm, lastnameForm)
        message_user = 'Gracias %s, su mensaje ha sido enviado correctamente.' % (nameForm)
        message_main = """ %s ha querido comunicarse y dejó el siguiente mensaje 
            \n %s \nLe interesa %s 
            \n Su correo es %s
            \n Su número de telefono es %s
            \n --- Este mensaje se ha enviado desde la página web https://www.dev2tech.xyz/   ---""" % (nameForm, messageForm, countryForm, emailForm, phoneForm)

        try:
            # Send to user
            # send_mail(subject_user, message_user, from_email_user, [emailForm])
            # Send to us
            send_mail(subject_main, message_main, from_email_main, ['jhernandez.18p@dev2tech.xyz'])
            # send_mail(subject_main, message_main, from_email_main, ['asesaludlaboral2727ca@gmail.com'])
            if str(lang) == 'es':
                url = es_url
            else:
                url = en_url

        except BadHeaderError:
            if str(lang) == 'es':
                url = es_error_url
            else:
                url = en_error_url
            return HttpResponseRedirect(url)
        return HttpResponseRedirect(url)

    return redirect(url)


def work(request):
    template = 'frontend/pages/work.html'
    context = {}
    lang = get_lang(request)
    es_url = 'trabajos'
    en_url = 'works'

    if str(lang) == 'es':
        pg_title = 'Trabajos'
        context['url'] = en_url
    else:
        pg_title = 'Works'
        context['url'] = es_url

    context['lang'] = lang
    context['pg_title'] = pg_title
    context['title'] = en_url
    return render(request,template,context)


def technology(request):
    template = 'frontend/pages/technologies.html'
    context = {}
    lang = get_lang(request)
    es_url = 'tecnologias'
    en_url = 'technologies'

    if str(lang) == 'es':
        pg_title = 'Trabajos'
        context['url'] = en_url
    else:
        pg_title = 'Works'
        context['url'] = es_url

    context['lang'] = lang
    context['pg_title'] = pg_title
    context['title'] = en_url
    return render(request,template,context)