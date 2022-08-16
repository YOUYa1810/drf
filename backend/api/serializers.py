from rest_framework import serializers


class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        read_only=True,
        view_name='product-detail',
        lookup_field='pk',
        )
    title = serializers.CharField(read_only=True)
    
class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    # other_products = serializers.SerializerMethodField(read_only=True)
    
    # def get_other_products(self, obj):
    #     user = obj
    #     my_product_qs = user.product_set.all()[:5]
    #     return ProductInlineSerializer(my_product_qs, many=True, context=self.context).data