# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *
from rest_framework import status




# ------------------ Property Category Views ------------------

class PropertyCategoryListCreateView(APIView):
    def get(self, request):
        try:
            categories = PropertyCategory.objects.all()
            serializer = PropertyCategorySerializer(categories, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = PropertyCategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PropertyCategoryDetailView(APIView):
    def get_object(self, property_category_id):
        return get_object_or_404(PropertyCategory, property_category_id=property_category_id)

    def get(self, request, property_category_id):
        try:
            category = self.get_object(property_category_id)
            serializer = PropertyCategorySerializer(category)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, property_category_id):
        try:
            category = self.get_object(property_category_id)
            serializer = PropertyCategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, property_category_id):
        try:
            category = self.get_object(property_category_id)
            category.delete()
            return Response({"message": "Property category deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# ------------------ Property Type Views ------------------

class PropertyTypeListCreateView(APIView):
    def get(self, request):
        try:
            types = PropertyType.objects.all()
            serializer = PropertyTypeSerializer(types, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = PropertyTypeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PropertyTypeDetailView(APIView):
    def get_object(self, property_type_id):
        return get_object_or_404(PropertyType, property_type_id=property_type_id)

    def get(self, request, property_type_id):
        try:
            prop_type = self.get_object(property_type_id)
            serializer = PropertyTypeSerializer(prop_type)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, property_type_id):
        try:
            prop_type = self.get_object(property_type_id)
            serializer = PropertyTypeSerializer(prop_type, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, property_type_id):
        try:
            prop_type = self.get_object(property_type_id)
            prop_type.delete()
            return Response({"message": "Property type deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# ------------------ Property Type by Category Name ------------------

class PropertyTypeByCategoryNameView(APIView):
    def get(self, request, category_name):
        try:
            category = PropertyCategory.objects.get(name__iexact=category_name)
            property_types = PropertyType.objects.filter(category=category)
            serializer = PropertyTypeSerializer(property_types, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PropertyCategory.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)







# ------------------ Property Type by Category ID ------------------

class PropertyTypeByCategoryIDView(APIView):
    def get(self, request, category_id):
        try:
            category = PropertyCategory.objects.get(property_category_id=category_id)
            property_types = PropertyType.objects.filter(category=category)
            serializer = PropertyTypeSerializer(property_types, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PropertyCategory.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)










# ------------------ Property Views ------------------

class PropertyListCreateView(APIView):
    def get(self, request):
        try:
            properties = Property.objects.all()
            serializer = PropertySerializer(properties, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = PropertySerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PropertyDetailView(APIView):
    def get_object(self, property_id):
        return get_object_or_404(Property, property_id=property_id)

    def get(self, request, property_id):
        try:
            property_instance = self.get_object(property_id)
            serializer = PropertySerializer(property_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, property_id):
        try:
            property_instance = self.get_object(property_id)
            serializer = PropertySerializer(property_instance, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, property_id):
        try:
            property_instance = self.get_object(property_id)
            property_instance.delete()
            return Response({"message": "Property deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


class PropertiesByUserID(APIView):
    def get(self, request, user_id):
        try:
            properties = Property.objects.filter(user_id=user_id)
            serializer = PropertySerializer(properties, many=True)  # <-- FIXED HERE
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# ------------------ Amenity Views ------------------

class AmenityListCreateView(APIView):
    def get(self, request):
        try:
            amenities = Amenity.objects.all()
            serializer = AmenitySerializer(amenities, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = AmenitySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AmenityDetailView(APIView):
    def get_object(self, amenity_id):
        return get_object_or_404(Amenity, amenity_id=amenity_id)

    def get(self, request, amenity_id):
        try:
            amenity = self.get_object(amenity_id)
            serializer = AmenitySerializer(amenity)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, amenity_id):
        try:
            amenity = self.get_object(amenity_id)
            serializer = AmenitySerializer(amenity, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, amenity_id):
        try:
            amenity = self.get_object(amenity_id)
            amenity.delete()
            return Response({"message": "Amenity deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from datetime import timedelta

from .models import Property
from .serializers import PropertySerializer  # Assuming you have a PropertySerializer

class LatestPropertiesAPIView(APIView):
    def get(self, request):
        # Calculate the date one month ago from today
        one_month_ago = timezone.now() - timedelta(days=30)

        # Fetch all properties created in the last month
        new_properties = Property.objects.filter(created_at__gte=one_month_ago)

        # Serialize the properties (use the appropriate serializer for your properties)
        serializer = PropertySerializer(new_properties, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
