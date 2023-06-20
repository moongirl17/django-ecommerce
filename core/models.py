from django.db import models

# Create your models here.
from django.db import models

class logo(models.Model):
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)
