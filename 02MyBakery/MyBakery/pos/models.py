from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=99)
    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=99)
    image = models.ImageField()
    price = models.IntegerField()
    in_stock = models.PositiveIntegerField()
    def __str__(self):
        return self.name
        
class Trasaction(models.Model):
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    amount = models.IntegerField()
    total_price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
