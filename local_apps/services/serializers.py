from rest_framework import serializers
from local_apps.services.models import Services


class ServiceSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Services model """
    class Meta:
        model = Services
        fields = (
            'service','name','nombre','en_slug','es_slug',
            'context','descripcion','objectives','objetivos',
            'benefits','beneficios','technology','tecnologia',
            'process','proceso','slogan','eslogan','en_checklist',
            'es_checklist','projects','related','created_at',
            'background_image','large_image','short_image',
        )