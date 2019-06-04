from django.urls import path
from .views import list_item, add_item, edit_item, sell_item

urlpatterns = [
    path('list' ,list_item, name='list_item'),
    path('add', add_item, name='add_item'),
    path('edit/<int:pk>', edit_item, name='edit_item'),
    path('sell/<int:pk>', sell_item, name='sell_item'),
]