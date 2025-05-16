from django.contrib import admin

# Register your models here.
from .models import Menu, MenuItem

class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1
    fk_name = 'parent'

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(MenuItem) 
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'menu', 'parent')
    list_filter = ('menu',)
    search_fields = ('name', 'url')
    inlines = [MenuItemInline]
