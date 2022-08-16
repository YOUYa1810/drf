from rest_framework.urls import path
from . import views

urlpatterns = [
    path('', views.SearchListView.as_view(), name='search')
]