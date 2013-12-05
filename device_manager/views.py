# -*- coding: UTF-8 -*-

from django.shortcuts import render
from device_manager.models import Device

def index(request):
    device_list = Device.objects.all()
    for device in device_list:
        status = device.device_status
        if(status == 1):
            device.status = "可用"
        elif(status == 2):
            device.status = "借出"
        elif(status == 3):
            device.status = "故障"
        else:
            device.status = "未知"
    
    context = {'device_list': device_list}
    return render(request, 'devices.html', context)