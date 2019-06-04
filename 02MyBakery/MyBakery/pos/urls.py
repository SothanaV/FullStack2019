from django.urls import path
from .views import list_item

urlpatterns = [
    path('list' ,list_item, name='list_item'),
]