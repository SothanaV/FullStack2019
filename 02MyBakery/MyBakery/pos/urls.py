from django.urls import path
from .views import list_item, add_item

urlpatterns = [
    path('list' ,list_item, name='list_item'),
    path('add', add_item, name='add_item'),
]