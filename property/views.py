

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *
from rest_framework import status




from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PropertyCategory
from .serializers import PropertyCategorySerializer
from django.shortcuts import get_object_or_404


class PropertyCategoryListCreateView(APIView):
    def get(self, request):
        categories = PropertyCategory.objects.all()
        serializer = PropertyCategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PropertyCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PropertyCategoryDetailView(APIView):
    def get_object(self, property_category_id):
        return get_object_or_404(PropertyCategory, property_category_id=property_category_id)

    def get(self, request, property_category_id):
        category = self.get_object(property_category_id)
        serializer = PropertyCategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, property_category_id):
        category = self.get_object(property_category_id)
        serializer = PropertyCategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, property_category_id):
        category = self.get_object(property_category_id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



from .models import PropertyType
from .serializers import PropertyTypeSerializer


class PropertyTypeListCreateView(APIView):
    def get(self, request):
        types = PropertyType.objects.all()
        serializer = PropertyTypeSerializer(types, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)  # Debug: Check incoming data
        serializer = PropertyTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PropertyTypeDetailView(APIView):
    def get_object(self, property_type_id):
        return get_object_or_404(PropertyType, property_type_id=property_type_id)

    def get(self, request, property_type_id):
        prop_type = self.get_object(property_type_id)
        serializer = PropertyTypeSerializer(prop_type)
        return Response(serializer.data)

    def put(self, request, property_type_id):
        prop_type = self.get_object(property_type_id)
        serializer = PropertyTypeSerializer(prop_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, property_type_id):
        prop_type = self.get_object(property_type_id)
        prop_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Property
from .serializers import PropertySerializer


class PropertyListCreateView(APIView):

    def get(self, request):
        properties = Property.objects.all()
        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PropertySerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PropertyDetailView(APIView):

    def get_object(self, property_id):
        return get_object_or_404(Property, property_id=property_id)

    def get(self, request, property_id):
        property_instance = self.get_object(property_id)
        serializer = PropertySerializer(property_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, property_id):
        property_instance = self.get_object(property_id)
        serializer = PropertySerializer(property_instance, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, property_id):
        property_instance = self.get_object(property_id)
        property_instance.delete()
        return Response({"message": "Property deleted successfully"}, status=status.HTTP_204_NO_CONTENT)







from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Amenity
from .serializers import AmenitySerializer
from django.shortcuts import get_object_or_404


class AmenityListCreateView(APIView):
    def get(self, request):
        amenities = Amenity.objects.all()
        serializer = AmenitySerializer(amenities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AmenitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AmenityDetailView(APIView):
    def get_object(self,amenity_id):
        return get_object_or_404(Amenity, amenity_id=amenity_id)

    def get(self, request, amenity_id):
        amenity = self.get_object(amenity_id)
        serializer = AmenitySerializer(amenity)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request,amenity_id):
        amenity = self.get_object(amenity_id)
        serializer = AmenitySerializer(amenity, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, amenity_id):
        amenity = self.get_object(amenity_id)
        amenity.delete()
        return Response({"message": "Amenity deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
