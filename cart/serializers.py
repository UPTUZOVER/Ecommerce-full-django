from rest_framework import serializers
from .models import Cart, CartItem
from products.models import Product
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from django.contrib.auth.models import AnonymousUser



class ProductSerializer(serializers.ModelSerializer):
    translations = TranslatedFieldsField(shared_model=Product)

    class Meta:
        model = Product
        fields = ['id', 'translations', 'price', 'image_main']
        ref_name = 'ProductSerializer'



class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    total_price = serializers.SerializerMethodField(method_name='total')
    
    

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'cart', 'quantity', 'total_price', 'is_active', 'created_date', 'modified_date']

    def total(self, cartitem:CartItem):
        return round(cartitem.product.price * cartitem.quantity,2)



class CartSerializer(serializers.ModelSerializer):
    id = serializers.CharField(max_length=255, read_only=True)
    cart_items = CartItemSerializer(many=True, read_only=True, source='cartitem_set')
    total_price = serializers.SerializerMethodField(method_name='main_total')

    class Meta:
        model = Cart
        fields = ('id', 'total_price', 'cart_items', 'created_date', 'modified_date')
        ref_name = 'CartSerializer'

    def create(self, validated_data):
        cart_items = validated_data.pop('cartitem_set', [])
        request = self.context.get('request', None)
        user = request.user if request else None
        if isinstance(user, AnonymousUser) or not user.is_authenticated:
            id = request.session.session_key if request else None
            if not id:
                id = request.session.create()
            cart, _ = Cart.objects.get_or_create(id=id)
        else:
            cart, _ = Cart.objects.get_or_create(user=user)

        for cart_item_data in cart_items:
            CartItem.objects.create(cart=cart, **cart_item_data)

        return cart

    def main_total(self, cart: Cart):
        items = cart.cartitem_set.all()
        total = sum([item.quantity * item.product.true_price for item in items])
        return round(total, 2)

class AddCartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    def save(self, **kwargs):
        cart_id = self.context["cart_id"]
        product_id = self.validated_data["product_id"]
        quantity = self.validated_data["quantity"]

        try:
            cart_item = CartItem.objects.get(cart_id=cart_id, product_id=product_id)
            cart_item.quantity += quantity
            cart_item.save()
            self.instance = cart_item
        except :
            self.instance = CartItem.objects.create(cart_id=cart_id, product_id=product_id, quantity=quantity)

        return self.instance

    class Meta:
        model = CartItem
        fields = ["id", 'product_id', 'quantity']
