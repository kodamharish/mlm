from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(PropertyCategory)
admin.site.register(PropertyType)
admin.site.register(Amenity)
admin.site.register(Property)
admin.site.register(PropertyImage)
admin.site.register(PropertyVideo)
