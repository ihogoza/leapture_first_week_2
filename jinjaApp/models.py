from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    tittle      = models.CharField(max_length=50)
    description = models.TextField(blank=True, null = True)
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    
    def get_absolute_url(self):
        return f"{self.id}/"
        # return reverse("product-detail", kwargs={"id": self.id})