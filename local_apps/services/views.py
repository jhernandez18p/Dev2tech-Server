from django.shortcuts import render
from rest_framework import viewsets
from local_apps.services.models import Services
from local_apps.services.serializers import ServiceSerializer
# Create your views here.

class ServicesViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Employee objects """
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer