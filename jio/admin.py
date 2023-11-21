from django.contrib import admin
from .models import jiomodel
# Register your models here.


class jioadmin(admin.ModelAdmin):
    list_display =['customer_id','mobile_number','recharge_amount','email','succes']

admin.site.register(jiomodel,jioadmin)
