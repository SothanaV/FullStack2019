from django.shortcuts import render,redirect
from .models import Category, Item, Trasaction
from .forms import ItemForm
# Create your views here.
def list_item(request):
    item = Item.objects.all().order_by('category')
    context = {'item':item}
    return render(request,'pos/listitem.html',context)

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
                form.save()
    form = ItemForm()
    context = {'form':form}
    return render(request,'pos/add.html',context)

def edit_item(request,pk):
    if request.method == 'POST':
        item = Item.objects.get(pk=pk)
        form = ItemForm(request.POST, request.FILES,instance=item)
        if form.is_valid():
                form.save()
        return redirect('list_item')
    form = ItemForm(instance=Item.objects.get(pk=pk))
    context = {'form':form}
    return render(request,'pos/edit.html',context)

def sell_item(request,pk):
    if request.method == 'POST':
        try:
            item = Item.objects.get(pk=pk)
            # item.in_stock = item.in_stock-int(request.POST['amount'])
            amount = int(request.POST['amount'])
            item.in_stock -= amount
            item.save()
            Trasaction.objects.create(
                    item=item,
                    amount = amount,
                    total_price = item.price*amount
                    )
        except Exception as e:
            print(e)
            raise e
        else:
            return redirect('list_item')
    else:
        item = Item.objects.get(pk=pk)
        context = {'item':item}
        return render(request,'pos/sell.html',context)