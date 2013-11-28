# -*- coding: UTF-8 -*-

from django.contrib import admin
from device_manager.models import Device, Order

# Register your models here.
admin.site.register(Device)
admin.site.register(Order)