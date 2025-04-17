from rest_framework import serializers
from .models import *


# serializers.py

from rest_framework import serializers
from .models import Property, PropertyImage, PropertyVideo


from rest_framework import serializers
from .models import PropertyCategory, PropertyType, Property

class PropertyCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyCategory
        fields = ['property_category_id', 'name']



class PropertyTypeSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=PropertyCategory.objects.all())

    class Meta:
        model = PropertyType
        fields = ['property_type_id', 'name', 'category']





from rest_framework import serializers
from .models import Property, PropertyImage, PropertyVideo, Amenity

class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['id', 'image']

class PropertyVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyVideo
        fields = ['id', 'video']

class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ['amenity_id', 'name']

class PropertySerializer(serializers.ModelSerializer):
    images = PropertyImageSerializer(many=True, read_only=True)
    videos = PropertyVideoSerializer(many=True, read_only=True)
    amenities = serializers.PrimaryKeyRelatedField(queryset=Amenity.objects.all(), many=True)

    class Meta:
        model = Property
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        images = request.FILES.getlist('images')
        videos = request.FILES.getlist('videos')

        amenities = validated_data.pop('amenities', [])
        property_instance = Property.objects.create(**validated_data)
        property_instance.amenities.set(amenities)

        for image in images:
            PropertyImage.objects.create(property=property_instance, image=image)

        for video in videos:
            PropertyVideo.objects.create(property=property_instance, video=video)

        return property_instance

    def update(self, instance, validated_data):
        request = self.context.get('request')
        images = request.FILES.getlist('images')
        videos = request.FILES.getlist('videos')

        amenities = validated_data.pop('amenities', [])

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        instance.amenities.set(amenities)

        # Replace old media
        PropertyImage.objects.filter(property=instance).delete()
        PropertyVideo.objects.filter(property=instance).delete()

        for image in images:
            PropertyImage.objects.create(property=instance, image=image)
        for video in videos:
            PropertyVideo.objects.create(property=instance, video=video)

        return instance

    
