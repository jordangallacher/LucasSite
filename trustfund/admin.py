from django.contrib import admin

# Register your models here.

from .models import Resource
from .models import Purchase

admin.site.register(Resource)
admin.site.register(Purchase)
