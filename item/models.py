from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    Name = models.CharField(max_length=255)

    class Meta:
        ordering = ('Name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.Name
    
class Items(models.Model):
    Name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    # name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='product_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name = 'items', on_delete=models.CASCADE)

    
    class Meta:
        ordering = ['Name']
        verbose_name_plural = 'Items'
    
    def __str__(self):
        return self.Name