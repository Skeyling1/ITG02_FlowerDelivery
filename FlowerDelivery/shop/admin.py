from django.contrib import admin

# Register your models here.
from .models import Good, Order


admin.site.register(Good)
admin.site.register(Order)
