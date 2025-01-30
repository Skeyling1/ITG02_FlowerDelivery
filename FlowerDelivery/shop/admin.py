from django.contrib import admin

# Register your models here.
from .models import Goods, Orders


admin.site.register(Goods)
admin.site.register(Orders)
