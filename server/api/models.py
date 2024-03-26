from django.db import models

# Create your models here.

class inventory (models.Model):
    thumbnail=models.ImageField(upload_to='thumbnail/images',null=True, blank=True)
    title=models.CharField(max_length=50, null=False, blank=False)
    category=models.CharField( max_length=50)
    description=models.TextField()
    price=models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

