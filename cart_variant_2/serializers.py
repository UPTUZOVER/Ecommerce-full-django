from rest_framework import serializers
from .models import Cart, CartItem
from .models import *
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from .models import Product_2, ProductImage
from categories.models import Category

class ProductImageSerializers(serializers.ModelSerializer): 
    class Meta:
        model = ProductImage
        fields = ['id', 'image']


class ProductSerializer_only(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Product_2)
    image = ProductImageSerializers(many=True, read_only=True)
    uploaded_images = serializers.ListField(child = serializers.ImageField(max_length=10000000000, allow_empty_file=False, use_url=False), 
                                            write_only=True, required=False)

    class Meta:
        model = Product_2
        fields = ('id', "title", 'categories', "cat", 'translations', 'image_main', 'count', 'price', "discount", 'true_price', 'image', 'updated_on', 'uploaded_images')

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        product = super().create(validated_data)
        for image in uploaded_images:
            ProductImage.objects.create(product=product, image=image)
        return product

    def update(self, instance, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        product = super().update(instance, validated_data)
        for image in uploaded_images:
            ProductImage.objects.create(product=product, image=image)
        return product                      

    def get_discount_percent(self, instance):
        if instance.discount:
            return int((instance.discount / instance.price) * 100)
        return 0

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.discount is not None:
            data['price'] = instance.true_price
        return data
    
    def get_categories_display(self, instance):
        return ", ".join([str(cat.title) for cat in instance.categories.all()])
    
class ProductSerializer(serializers.ModelSerializer):
    translations = TranslatedFieldsField(shared_model=Product_2)

    class Meta:
        model = Product_2
        fields = ['id', 'translations', 'price', 'image_main']



class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    total_price = serializers.SerializerMethodField(method_name='total')

    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'quantity', 'total_price', 'is_active', 'created_date', 'modified_date', 'product']
        ref_name = 'CartItemSerializer'

   
    


    def total(self, cartitem:CartItem):
        return round(cartitem.product.price * cartitem.quantity,2)






class CartSerializer(serializers.ModelSerializer):
    id = serializers.CharField(max_length=255, read_only=True)
    cart_items = CartItemSerializer(many=True, read_only=True, source='cartitem_set')
    total_price = serializers.SerializerMethodField(method_name='main_total')


    def create(self, validated_data):
        cart_items = validated_data.pop('cart_items', [])
        request = self.context.get('request', None)
        id = request.session.session_key if request else None
        if not id:
            id = request.session.create()
        cart, _ = Cart.objects.get_or_create(id=id)

        for cart_item_data in cart_items:
            CartItem.objects.create(cart=cart, **cart_item_data)

        return cart

    class Meta:
        model = Cart
        fields = ('id', 'total_price', 'cart_items', 'created_date', 'modified_date')

    def main_total(self, cart: Cart):
        items = cart.cartitem_set.all()
        total = sum([item.quantity * item.product.price for item in items])
        return round(total,2)


















