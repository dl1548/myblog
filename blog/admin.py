# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Article

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'date_time', 'content']

admin.site.register(Article,PostAdmin)
