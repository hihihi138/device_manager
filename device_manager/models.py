# -*- coding: UTF-8 -*-

from django.db import models
from django.contrib.auth.models import User
import datetime

class Device(models.Model):
    device_name = models.CharField(max_length=50)
    device_brand = models.CharField(max_length=50)
    device_price = models.FloatField(blank=True)
    device_user = models.ForeignKey(User)
    device_imei = models.BigIntegerField(max_length=15)
    device_status = models.IntegerField(max_length=1)
    device_reg_date = models.DateTimeField(default=datetime.datetime.now())
    
class Order(models.Model):
    order_starttime = models.DateTimeField()
    order_endtime = models.DateTimeField()
    order_time = models.DateTimeField(default=datetime.datetime.now())
    order_from_user = models.CharField(max_length=50)
    order_to_user = models.CharField(max_length=50)
    order_device = models.ForeignKey(Device)
    order_comment = models.TextField()