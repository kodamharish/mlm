from rest_framework import serializers
from .models import *

# class PropertySerializer(serializers.ModelSerializer):
#     class Meta:
#         model= Property
#         fields ='__all__'


# serializers.py

from rest_framework import serializers
from .models import Property, PropertyImage, PropertyVideo


from rest_framework import serializers
from .models import PropertyCategory, PropertyType, Property

class PropertyCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyCategory
        fields = ['property_category_id', 'name']

# class PropertyTypeSerializer(serializers.ModelSerializer):
#     category = PropertyCategorySerializer(read_only=True)

#     class Meta:
#         model = PropertyType
#         fields = ['id', 'name', 'category']


class PropertyTypeSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=PropertyCategory.objects.all())

    class Meta:
        model = PropertyType
        fields = ['property_type_id', 'name', 'category']



# class PropertyImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PropertyImage
#         fields = ['id', 'image']

# class PropertyVideoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PropertyVideo
#         fields = ['id', 'video']

# class PropertySerializer(serializers.ModelSerializer):
#     images = PropertyImageSerializer(many=True, required=False)
#     videos = PropertyVideoSerializer(many=True, required=False)

#     class Meta:
#         model = Property
#         fields = '__all__'

#     def create(self, validated_data):
#         images_data = self.context['request'].FILES.getlist('images')
#         videos_data = self.context['request'].FILES.getlist('videos')
#         property_instance = Property.objects.create(**validated_data)

#         for image in images_data:
#             PropertyImage.objects.create(property=property_instance, image=image)

#         for video in videos_data:
#             PropertyVideo.objects.create(property=property_instance, video=video)

#         return property_instance


# from rest_framework import serializers
# from .models import Property, PropertyImage, PropertyVideo

# class PropertyImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PropertyImage
#         fields = ['id', 'image']


# class PropertyVideoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PropertyVideo
#         fields = ['id', 'video']


# class PropertySerializer(serializers.ModelSerializer):
#     images = serializers.ListField(
#         child=serializers.ImageField(), write_only=True, required=False
#     )
#     videos = serializers.ListField(
#         child=serializers.FileField(), write_only=True, required=False
#     )

#     property_images = PropertyImageSerializer(source='propertyimage_set', many=True, read_only=True)
#     property_videos = PropertyVideoSerializer(source='propertyvideo_set', many=True, read_only=True)

#     class Meta:
#         model = Property
#         fields = '__all__'
#         extra_fields = ['images', 'videos', 'property_images', 'property_videos']

#     def create(self, validated_data):
#         images = self.context['request'].FILES.getlist('images')
#         videos = self.context['request'].FILES.getlist('videos')

#         property_instance = Property.objects.create(**validated_data)

#         for img in images:
#             PropertyImage.objects.create(property=property_instance, image=img)

#         for vid in videos:
#             PropertyVideo.objects.create(property=property_instance, video=vid)

#         return property_instance

#     def update(self, instance, validated_data):
#         request = self.context.get('request')
#         images = request.FILES.getlist('images')
#         videos = request.FILES.getlist('videos')

#         # Update property fields
#         for attr, value in validated_data.items():
#             setattr(instance, attr, value)
#         instance.save()

#         # Delete old media
#         PropertyImage.objects.filter(property=instance).delete()
#         PropertyVideo.objects.filter(property=instance).delete()

#         # Add new media
#         for img in images:
#             PropertyImage.objects.create(property=instance, image=img)

#         for vid in videos:
#             PropertyVideo.objects.create(property=instance, video=vid)

#         return instance




# from rest_framework import serializers
# from .models import Property, PropertyImage, PropertyVideo, Amenity

# class PropertyImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PropertyImage
#         fields = ['id', 'image']  # Add other fields as necessary

# class PropertyVideoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PropertyVideo
#         fields = ['id', 'video']  # Add other fields as necessary

# class AmenitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Amenity
#         fields = ['id', 'name']  # Add other fields as necessary

# class PropertySerializer(serializers.ModelSerializer):
#     images = PropertyImageSerializer(many=True, required=False)
#     videos = PropertyVideoSerializer(many=True, required=False)
#     amenities = AmenitySerializer(many=True, required=False)
#     class Meta:
#         model = Property
#         fields = '__all__'
#         extra_fields = ['images', 'videos', 'amenities']


#     def create(self, validated_data):
#         # Extract images, videos, and amenities from validated_data
#         images = validated_data.pop('images', [])
#         videos = validated_data.pop('videos', [])
#         amenities_data = validated_data.pop('amenities', [])

#         # Create the Property instance
#         property_instance = Property.objects.create(**validated_data)

#         # Handle many-to-many fields
#         if amenities_data:
#             amenity_instances = Amenity.objects.filter(id__in=[amenity['id'] for amenity in amenities_data])
#             property_instance.amenities.set(amenity_instances)

#         # Create and associate PropertyImage and PropertyVideo
#         for img in images:
#             PropertyImage.objects.create(property=property_instance, image=img['image'])

#         for vid in videos:
#             PropertyVideo.objects.create(property=property_instance, video=vid['video'])

#         return property_instance

#     def update(self, instance, validated_data):
#         # Extract images, videos, and amenities from validated_data
#         images = validated_data.pop('images', [])
#         videos = validated_data.pop('videos', [])
#         amenities_data = validated_data.pop('amenities', [])

#         # Update the Property instance fields
#         for attr, value in validated_data.items():
#             setattr(instance, attr, value)
        
#         # Handle many-to-many fields
#         if amenities_data:
#             amenity_instances = Amenity.objects.filter(id__in=[amenity['id'] for amenity in amenities_data])
#             instance.amenities.set(amenity_instances)

#         instance.save()

#         # Handle media (images/videos)
#         PropertyImage.objects.filter(property=instance).delete()
#         PropertyVideo.objects.filter(property=instance).delete()

#         # Recreate images and videos
#         for img in images:
#             PropertyImage.objects.create(property=instance, image=img['image'])
        
#         for vid in videos:
#             PropertyVideo.objects.create(property=instance, video=vid['video'])

#         return instance


# from rest_framework import serializers
# from .models import Amenity

# class AmenitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Amenity
#         fields = '__all__'







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

    
