from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

class Category(models.Model):
    category = models.CharField(max_length=40)

    def __str__(self):
        return self.category
    
class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.category} - {self.name}"
    
class Movement(models.Model):
    TRUCKR2 = 'R2'
    TRUCKB2 = 'B2'
    TRUCK_UNIT_CHOICES = [
        (TRUCKR2, 'Carro R2'),
        (TRUCKB2, 'Carro B2'),
    ]
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='movements',
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='related_movements',
    )
    responsible = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    unit = models.CharField(
        max_length=2,
        choices=TRUCK_UNIT_CHOICES,
        default=TRUCKB2,
    )
    quantity = models.BigIntegerField()
    motive = models.TextField()

    def __str__(self):
        return f"{self.item} - {self.quantity} unidades - motivo: {self.motive}"

    def get_absolute_url(self):
        return reverse('your_app:your_view_name', args=[str(self.id)])
    
    def save(self, *args, **kwargs):
        super(Movement, self).save(*args, **kwargs)
        inventory, created = Inventory.objects.get_or_create(item=self.item)
        inventory.quantity = Movement.objects.filter(item=self.item).aggregate(models.Sum('quantity'))['quantity__sum'] or 0
        inventory.save()
    
class Inventory(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='inventories')
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.item} - {self.quantity}"