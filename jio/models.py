from django.db import models

# Create your models here.

class jiomodel(models.Model):
    customer_id=models.IntegerField(primary_key=True)
    mobile_number=models.BigIntegerField()
    recharge_amount=models.IntegerField()
    email=models.EmailField()
    succes=models.BooleanField()