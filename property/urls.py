from django.urls import path
from .views import *

urlpatterns = [
    
    path('property/', PropertyListCreateView.as_view(), name='property'),
    path('property/<int:property_id>/', PropertyDetailView.as_view(), name='property_details'),
    
]