# -*- coding: UTF-8 -*-

from django.shortcuts import render
from device_manager.models import Device

def index(request):
    device_list = Device.objects.all()
    context = {'device_list': device_list}
    return render(request, 'devices.html', context)