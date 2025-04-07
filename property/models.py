from django.db import models
from decimal import Decimal
import os

def property_image_upload_path(instance, filename):
    """
    Generate a dynamic file path for storing property images.
    Images will be stored under 'property/{property_type}/filename.ext'
    """
    property_type_folder = instance.property_type.lower().replace(" ", "_")  # Convert to lowercase & replace spaces
    return os.path.join(f"property/{property_type_folder}/", filename)  



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
#     property_value = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, default=0.00)
#     ownership_type = models.CharField(max_length=100, blank=True, null=True)
#     property_image = models.ImageField(upload_to=property_image_upload_path, blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def save(self, *args, **kwargs):
#         # Ensure valid calculations for price_per_unit
#         if self.property_value and self.no_of_investors and self.no_of_investors > 0:
#             self.price_per_unit = self.property_value / Decimal(self.no_of_investors)
#         else:
#             self.price_per_unit = Decimal(0.00)

#         super().save(*args, **kwargs)

#     def __str__(self):
#         return f"{self.property_id}"


class Property(models.Model):
    property_id = models.AutoField(primary_key=True)
    property_name = models.CharField(max_length=150, blank=True, null=True)
    property_type = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    pin_code = models.CharField(max_length=15, blank=True, null=True)

    # Owner Details
    owner_name = models.CharField(max_length=150, blank=True, null=True)
    owner_contact = models.CharField(max_length=15, blank=True, null=True)
    owner_email = models.EmailField(blank=True, null=True)

    # Agent Details
    agent_id = models.CharField(max_length=50, blank=True, null=True)

    # Geolocation
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    # Property Details
    property_value = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, default=0.00)
    ownership_type = models.CharField(max_length=100, blank=True, null=True)
    property_image = models.ImageField(upload_to=property_image_upload_path, blank=True, null=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.property_id} - {self.property_name}"


