from rest_framework import viewsets, mixins

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    '''
    get -> list -> queryset
    get -> retrieve -> product instance detail view
    post -> create -> new instance
    put -> update
    patch -> partial update
    delete -> destroy
    '''
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    
class ProductGenericViewSet(
    mixins.ListModelMixin, 
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    '''
    get -> list -> queryset
    get -> retrieve -> product instance detail view
    '''
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
# as view    
# product_list_view = ProductGenericViewSet.as_view({'get': 'list'})
# product_detial_view = ProductGenericViewSet.as_view({'get': 'retrieve'})