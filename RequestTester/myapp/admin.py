from django.contrib import admin
from .models import Person
# Register your models here.
@admin.register(Person)
class PeraonAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Person._meta.fields]