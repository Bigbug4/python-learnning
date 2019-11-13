#!/usr/bin/env python3
# coding=utf-8

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
