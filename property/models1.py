# from django.db import models
# from decimal import Decimal
# import os

# def property_image_upload_path(instance, filename):
#     """
#     Generate a dynamic file path for storing property images.
#     Images will be stored under 'property/{property_type}/filename.ext'
#     """
#     property_type_folder = instance.property_type.lower().replace(" ", "_")  # Convert to lowercase & replace spaces
#     return os.path.join(f"property/{property_type_folder}/", filename)  





# class Property(models.Model):
#     property_id = models.AutoField(primary_key=True)
#     property_name = models.CharField(max_length=150, blank=True, null=True)
#     property_type = models.CharField(max_length=100, blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     address = models.TextField(blank=True, null=True)
#     city = models.CharField(max_length=100, blank=True, null=True)
#     state = models.CharField(max_length=100, blank=True, null=True)
#     country = models.CharField(max_length=100, blank=True, null=True)
#     pin_code = models.CharField(max_length=15, blank=True, null=True)

#     # Owner Details
#     owner_name = models.CharField(max_length=150, blank=True, null=True)
#     owner_contact = models.CharField(max_length=15, blank=True, null=True)
#     owner_email = models.EmailField(blank=True, null=True)

#     # Agent Details
#     agent_id = models.CharField(max_length=50, blank=True, null=True)

#     # Geolocation
#     latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
#     longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

#     # Property Details
#     property_value = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, default=0.00)
#     ownership_type = models.CharField(max_length=100, blank=True, null=True)
#     property_image = models.ImageField(upload_to=property_image_upload_path, blank=True, null=True)

#     # Timestamps
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.property_id} - {self.property_name}"









from django.db import models

class PropertyCategory(models.Model):
    property_category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class PropertyType(models.Model):
    property_type_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(PropertyCategory, on_delete=models.CASCADE, related_name='types')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.category.name} - {self.name}"


class Amenity(models.Model):
    amenity_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Property(models.Model):
    LOOKING_TO_CHOICES = [
        ('sell', 'Sell'),
        ('rent', 'Rent / Lease'),
        ('pg', 'PG'),
    ]

    FACING_CHOICES = [
        ('east', 'East'),
        ('west', 'West'),
        ('north', 'North'),
        ('south', 'South'),
        ('north_east', 'North-East'),
        ('north_west', 'North-West'),
        ('south_east', 'South-East'),
        ('south_west', 'South-West'),
    ]

    property_id = models.AutoField(primary_key=True)


    # Basic Info
    looking_to = models.CharField(max_length=10, choices=LOOKING_TO_CHOICES)
    category = models.ForeignKey('PropertyCategory', on_delete=models.SET_NULL, null=True)
    property_type = models.ForeignKey('PropertyType', on_delete=models.SET_NULL, null=True)
    property_title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    # Location Details
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=15)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    # Area and Dimensions
    plot_area_sqft = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    builtup_area_sqft = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    length_ft = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    breadth_ft = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    
    # Property Structure
    number_of_floors = models.PositiveIntegerField(blank=True, null=True)
    number_of_open_sides = models.PositiveIntegerField(blank=True, null=True)
    number_of_roads = models.PositiveIntegerField(blank=True, null=True)
    road_width_1_ft = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    road_width_2_ft = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    # Facing
    facing = models.CharField(max_length=20, choices=FACING_CHOICES, blank=True, null=True)

    # Ownership & Financials
    ownership_type = models.CharField(max_length=100, blank=True, null=True)
    property_value = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, default=0.00)

    # Amenities
    amenities = models.ManyToManyField(Amenity, blank=True)

    # Additional Info
    property_uniqueness = models.TextField(blank=True, null=True)
    location_advantages = models.TextField(blank=True, null=True)
    other_features = models.TextField(blank=True, null=True)

    # Owner Details
    owner_name = models.CharField(max_length=150, blank=True, null=True)
    owner_contact = models.CharField(max_length=15, blank=True, null=True)
    owner_email = models.EmailField(blank=True, null=True)

    # Agent
    agent_id = models.CharField(max_length=50, blank=True, null=True)

    # User
    user_id = models.CharField(max_length=50, blank=True, null=True)

    # Single main image
    property_image = models.ImageField(upload_to='property_images/', blank=True, null=True)

    # Flags
    is_featured = models.BooleanField(default=False)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.property_title or 'Untitled'} - {self.property_type.name if self.property_type else 'N/A'}"


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/property_images/')

    def __str__(self):
        return f"Image for {self.property}"


class PropertyVideo(models.Model):
    property = models.ForeignKey(Property, related_name='videos', on_delete=models.CASCADE)
    video = models.FileField(upload_to='media/property_videos/')

    def __str__(self):
        return f"Video for {self.property}"

