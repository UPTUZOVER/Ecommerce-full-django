from django.db import models
from decimal import Decimal
from django.db import models
from django.utils.translation import gettext_lazy as _  # Lokalizatsiya uchun _ funksiyasini import qilamiz
import uuid
from parler.models import TranslatableModel, TranslatedFields
from categories.models import Category

class Product_2(TranslatableModel):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    translations = TranslatedFields(
        title=models.CharField(max_length=200, unique=True, verbose_name=("Mahsul nomi")),
        description=models.TextField(blank=True, verbose_name=("Mahsul tavsifi")),
    )
    categories = models.ForeignKey(Category, verbose_name=("Turkum"), on_delete=models.CASCADE)
    image_main = models.ImageField(upload_to='images/', verbose_name=("Asosiy rasmi"), null=True, blank=True)
    count = models.IntegerField(null=True, verbose_name=("Maxulot miqdori"))
    price = models.IntegerField(verbose_name=("Maxulot narxi"), null=True, default=0)
    discount = models.IntegerField(verbose_name=("chegirmna"), null=True, blank=True)
    true_price = models.DecimalField(verbose_name=("oxirgi narx"), max_digits=10, decimal_places=2, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, verbose_name=("Yangilangan sana"))
    created_on = models.DateTimeField(auto_now_add=True, verbose_name=("Yaratilgan sana"))


    def save(self, *args, **kwargs):
        if self.discount is not None and self.price is not None:
            self.true_price = self.price - (self.price * self.discount / 100)
        super().save(*args, **kwargs)
            
    def cat(self):
        return self.categories.title

    class Meta:
        ordering = ['-created_on'] 
        verbose_name = _("Product") 
        verbose_name_plural = _("Products")  

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(Product_2, on_delete=models.CASCADE, related_name="image")
    image = models.ImageField(upload_to="cart_variant_2/images/", default='', null=True, blank=True)


class Cart(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_total_price(self):
        total = Decimal(0)
        for item in self.cartitem_set.all():
            total += item.get_total_price()
        return total

    def get_total_items(self):
        return self.cartitem_set.count()

    def __str__(self):
        return f"Cart {self.id}"

class CartItem(models.Model):
    product = models.ForeignKey(Product_2, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE )
    quantity = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_total_price(self):
        return self.product.price * self.quantity


    def get_cart_items(self):
        return self.cartitem_set.all()

    def __str__(self):
        return f"{self.quantity} x {self.product.title}"