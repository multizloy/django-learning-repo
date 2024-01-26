from django.contrib import admin
from .models import Categories, Products

# Register your models here.


# admin.site.register(Categories)
# admin.site.register(Products)
@admin.register(Categories)
class Admin_Categories(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
@admin.register(Products)
class Admin_Products(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}