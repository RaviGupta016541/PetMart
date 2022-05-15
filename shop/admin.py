from django.contrib import admin

# Register your models here.
from .models import Adds, Contact
admin.site.register(Adds)
admin.site.register(Contact)