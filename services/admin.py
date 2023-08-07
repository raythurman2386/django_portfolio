from django.contrib import admin

from services.models import Summary, Service, Contact

# Register your models here.
admin.site.register(Summary)
admin.site.register(Service)
admin.site.register(Contact)
