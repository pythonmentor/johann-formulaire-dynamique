from django.contrib import admin

from . import models 

admin.site.register(models.Country)
admin.site.register(models.Supplier)
admin.site.register(models.Brand)