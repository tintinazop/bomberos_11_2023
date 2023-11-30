from django import forms
from django.contrib import admin
from .models import Category, Item, Movement, Inventory

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Movement)
admin.site.register(Inventory)