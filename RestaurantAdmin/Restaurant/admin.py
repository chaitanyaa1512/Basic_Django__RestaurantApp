from django.contrib import admin
from Restaurant.models import Food
from Restaurant.models import Tables
from Restaurant.models import Waiters
from Restaurant.models import Orders

# Register your models here.
admin.site.register(Food)
admin.site.register(Tables)
admin.site.register(Waiters)
admin.site.register(Orders)