from django.contrib.auth.models import User
from django.db import models
from decimal import Decimal
# from django.urls import reverse
# from django.conf import settings






class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=3, default=Decimal('6.00'))
    # slug = models.SlugField(unique=True, null=True)
    discount_price = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    # label = models.CharField(max_length=10, default='Default Label')
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # def __str__(self):
    #     return self.name
    
    # def get_absolute_url(self):
    #     return reverse("item:detail", kwargs={
    #         "slug": self.slug
    #         })
    
    # def get_add_to_cart_url(self):
    #     return reverse("item:add-to-cart", kwargs={
    #         "slug": self.slug
    #         })
    
    # def get_remove_from_cart_url(self):
    #     return reverse("item:remove-from-cart", kwargs={
    #         "slug": self.slug
            # })
    
    @property
    def get_price(self):
        if self.discount_price:
            return self.discount_price
        else:
            return self.price
        
    @property
    def discount_percentage(self):
        if self.discount_price:
            return round(((self.price - self.discount_price) / self.price) * 100)
        else:
            return 0

# class OrderItem(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     ordered = models.BooleanField(default=False)
#     produk_item = models.ForeignKey(Item, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)

#     def __str__(self):
#         return f"{self.quantity} of {self.produk_item.nama_produk}"

#     def get_total_harga_item(self):
#         return self.quantity * self.produk_item.harga
    
#     def get_total_harga_diskon_item(self):
#         return self.quantity * self.produk_item.harga_diskon

#     def get_total_hemat_item(self):
#         return self.get_total_harga_item() - self.get_total_harga_diskon_item()
    
#     def get_total_item_keseluruan(self):
#         if self.produk_item.harga_diskon:
#             return self.get_total_harga_diskon_item()
#         return self.get_total_harga_item()
    
#     def get_total_hemat_keseluruhan(self):
#         if self.produk_item.harga_diskon:
#             return self.get_total_hemat_item()
#         return 0