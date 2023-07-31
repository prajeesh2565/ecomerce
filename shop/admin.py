from django.contrib import admin
from .models import category,product
# Register your models here.

class Categoryadmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(category,Categoryadmin)

class Productadmin(admin.ModelAdmin):
    list_display = ('name','price','stock','available','created','updated')
    list_editable = ('price','stock','available')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(product,Productadmin)
