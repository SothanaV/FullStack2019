from django.contrib import admin
from .models import Category,Item,Trasaction
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Category._meta.fields]

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Item._meta.fields]

@admin.register(Trasaction)
class TrasactionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Trasaction._meta.fields]
