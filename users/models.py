from django.db import models

from django.db import models
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.contrib.auth.hashers import make_password


def temp_directory_path(instance, filename):
    """Save files temporarily in a 'temp' folder."""
    ext = filename.split('.')[-1]
    return f"temp/{filename.split('.')[0]}.{ext}"


class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.role_id}"

class User(models.Model):
    user_id = models.AutoField(primary_key=True) 
    roles = models.ManyToManyField('Role')   
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)  
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20,null=True, blank=True)
    # Store files inside a temp folder first
    image   = models.ImageField(upload_to=temp_directory_path, blank=True, null=True) 
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    pin_code = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    pan_number = models.CharField(max_length=10, blank=True, null=True)
    aadhaar_number = models.CharField(max_length=12, blank=True, null=True)
    # Store PAN & Aadhaar files inside a temp folder first
    pan = models.FileField(upload_to=temp_directory_path, blank=True, null=True)
    aadhaar = models.FileField(upload_to=temp_directory_path, blank=True, null=True)
    kyc_status = models.CharField(max_length=100, blank=True, null=True)
    account_holder_name = models.CharField(max_length=255, blank=True, null=True)
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    branch_name = models.CharField(max_length=255, blank=True, null=True)
    account_number = models.CharField(max_length=100,blank=True, null=True)
    account_type = models.CharField(max_length=100,blank=True, null=True)
    ifsc_code = models.CharField(max_length=60, blank=True, null=True)
    nominee_reference_to = models.CharField(max_length=50,blank=True, null=True)
    referral_id = models.CharField(max_length=50,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def save(self, *args, **kwargs):
        new_user = not self.pk  # Check if user is new
        if new_user and not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)  # Save to generate user_id
        if new_user:
            self.move_files_to_user_folder()
    def move_files_to_user_folder(self):
        """Move files from temp folder to user_id folder after user creation."""
        for file_field in ['image', 'pan', 'aadhaar']:
            file_instance = getattr(self, file_field)
            if file_instance:
                old_path = file_instance.name
                ext = old_path.split('.')[-1]
                new_path = f"{self.user_id}/{file_field}.{ext}"
                # Move file if the path is still in temp
                if old_path.startswith("temp/") and old_path != new_path:
                    with default_storage.open(old_path, 'rb') as file_content:
                        default_storage.save(new_path, ContentFile(file_content.read()))
                    default_storage.delete(old_path)  # Remove temp file
                    # Update file path and save
                    setattr(self, file_field, new_path)
                    super().save(update_fields=[file_field])  # Save again to update path
    def __str__(self):
        return f"{self.user_id}"
