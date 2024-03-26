from django.db import models

# Create your models here.

class inventory (models.Model):
    thumbnail=models.ImageField(upload_to='thumbnail/images',null=True, blank=True)
    title=models.CharField(max_length=50, null=False, blank=False)
    category=models.CharField( max_length=50)
    in_stock=models.IntegerField(null=True, blank=True)
    price=models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

