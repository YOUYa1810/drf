from rest_framework import serializers
from api.serializers import UserPublicSerializer
from rest_framework.reverse import reverse
from .models import Product
from . import validators 


class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        read_only=True,
        view_name='product-detail',
        lookup_field='pk',
        )
    title = serializers.CharField(read_only=True)
    
    
class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True)
    related_product = ProductInlineSerializer(source='user.product_set.all', read_only=True, many=True)
    url = serializers.HyperlinkedIdentityField(
        read_only=True,
        view_name='product-detail',
        lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only=True)
    title = serializers.CharField(validators=[validators.validate_title, validators.unique_product_title])
    name = serializers.CharField(source='title', read_only=True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    
    # email = serializers.EmailField(write_only=True)
    
    class Meta:
        model = Product
        fields = [
            'owner',
            'related_product',
            'url',
            'edit_url',
            'pk',
            'title',
            'name',
            'content',
            'price',
            'sale_price',
            'my_discount',
            # 'email',
        ]
    
    # def validate_title(self, value):
    #     request = self.context.get('request')
    #     user = request.user
    #     qs = Product.objects.filter(user=user, title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f'{value} is already a product name')
    #     return value
    
    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('product-update', kwargs={'pk': obj.pk}, request=request)
        
    def get_my_discount(self, obj): # assume a instance is attached to it
        return obj.get_discount()
