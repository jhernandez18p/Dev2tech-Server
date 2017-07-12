from django.contrib import admin
from local_apps.services.models import (Services)

# Register your models here.
@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
	list_display = ["id","name","technology"]
	list_display_links = ['id']
	list_editable = ["technology"]
	list_filter = ["technology"]
	search_fields = ["name"]
	
	class Meta:
		model = Services