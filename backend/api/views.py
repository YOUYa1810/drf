from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    drf api view
    """
    # request -> HttpRequest -> django
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print(serializer.data)
        data = serializer.data
    # instance = Product.objects.all().order_by("?").first()
    # data = {}
    # if instance:
    #     """
    #     serialization:
    #     models instance(model_data)
    #     turn a python dict
    #     return json to client
    #     """
       
    #     data = ProductSerializer(instance).data
    #request.body
    # body = request.body # byte string of json data
    # data = {}
    # try:
    #     data =  json.loads(body) # string of json data -> python dict
    # except:
    #     pass
    # print(data)
    # print(request.GET)
    # data['params'] = dict(request.GET)
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type
    
    # allow dict as a aurgement to json
    return Response(data)
