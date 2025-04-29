from django.urls import path
from .views import *

urlpatterns = [



    path('property-categories/', PropertyCategoryListCreateView.as_view(), name='property-category-list-create'),
    path('property-categories/<int:property_category_id>/', PropertyCategoryDetailView.as_view(), name='property-category-detail'),
    
    path('property-types/', PropertyTypeListCreateView.as_view(), name='property-type-list-create'),
    path('property-types/<int:property_type_id>/', PropertyTypeDetailView.as_view(), name='property-type-detail'),
    path('property-types/category-name/<str:category_name>/', PropertyTypeByCategoryNameView.as_view(), name='property-types-by-category-name'),
    path('property-types/category-id/<int:category_id>/', PropertyTypeByCategoryIDView.as_view(), name='property-types-by-category-id'),


    path('amenities/', AmenityListCreateView.as_view(), name='amenity-list-create'),
    path('amenities/<int:amenity_id>/', AmenityDetailView.as_view(), name='amenity-detail'),
    
    path('property/', PropertyListCreateView.as_view(), name='property'),
    path('property/<int:property_id>/', PropertyDetailView.as_view(), name='property_details'),
    
    path('properties/user-id/<int:user_id>/', PropertiesByUserID.as_view(), name='properties-user-id'),
    path('latest-properties/', LatestPropertiesAPIView.as_view(), name='new-properties'),

    
]