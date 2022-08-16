from rest_framework.routers import DefaultRouter
from rest_framework.urls import path
import products.viewsets as viewsets

# http://127.0.0.1:8000/api/v2/products-abc/
router = DefaultRouter()
# router.register('products-abc', viewsets.ProductViewSet, basename='products')
router.register('products-abc', viewsets.ProductGenericViewSet, basename='products')
# print(router.urls)
urlpatterns = router.urls


# http://127.0.0.1:8000/api/v2/
# urlpatterns = [
#     path('<int:pk>/', viewsets.product_detial_view),
#     path('', viewsets.product_list_view)
# ]