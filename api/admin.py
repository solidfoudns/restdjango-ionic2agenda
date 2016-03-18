from django.contrib import admin

# Register your models here.
from .models import Orden

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    pass
