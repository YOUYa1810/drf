from rest_framework import generics, mixins
from .models import Product
from .serializers import ProductSerializer
from api.mixins import (
    UserQuerySetMixin,
    StuffEditorPermissionMixin)

class ProductListCreateAPIView(
    UserQuerySetMixin,
    StuffEditorPermissionMixin,
    generics.ListCreateAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    allow_superuser_view = True
    
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        email = serializer.validated_data.pop('email')
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = title
        serializer.save(user=self.request.user, content=content)
        # send a django signal

           
class ProductDetailAPIView(
    UserQuerySetMixin,
    StuffEditorPermissionMixin,
    generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_fields = 'pk'
    
    
class ProductUpdateAPIView(
    UserQuerySetMixin,
    StuffEditorPermissionMixin,
    generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_fields = 'pk'
    
    def perform_update(selrf, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
    

class ProductDeleteAPIView(
    UserQuerySetMixin,
    StuffEditorPermissionMixin,
    generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_fields = 'pk'
    
    def perform_destroy(selrf, instance):
        super().perform_destroy(instance)
        
        
"""
mixins can do all CRUD
"""        
class ProductMixnView(
    UserQuerySetMixin,
    StuffEditorPermissionMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin, 
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_ = 'pk'
    
    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
 
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = 'cooooool'
        serializer.save(user=self.request.user, content=content)