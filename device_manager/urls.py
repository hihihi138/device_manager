# -*- coding: UTF-8 -*-

'''
Created on 2013年11月28日

@author: bj_liujun
'''

from django.conf.urls import patterns, url

from device_manager import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)