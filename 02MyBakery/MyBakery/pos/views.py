from django.shortcuts import render
from .models import Category, Item, Trasaction
from .forms import ItemForm
# Create your views here.
def list_item(request):
    item = Item.objects.all().order_by('category')
    context = {'item':item}
    return render(request,'pos/listitem.htm',context)

def add_item(request):
    form = ItemForm()
    context = {'form':form}
    return render(request,'pos/edit.htm',context)