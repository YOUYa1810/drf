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
    url = serializers.HyperlinkedIdentityField(
        read_only=True,
        view_name='product-detail',
        lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only=True)
    title = serializers.CharField(validators=[validators.validate_title, validators.unique_product_title])
    name = serializers.CharField(source='title', read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'owner',
            'url',
            'edit_url',
            'pk',
            'title',
            'name',
            'content',
            'price',
            'sale_price',
        ]
    
    
    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('product-update', kwargs={'pk': obj.pk}, request=request)
        
