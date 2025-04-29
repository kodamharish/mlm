from django.db import models
from users.models import *

# Create your models here.
# class SubscriptionPlan(models.Model):
#     plan_id = models.AutoField(primary_key=True)  # Primary key
#     plan_name = models.CharField(max_length=100, unique=True)  # Plan name (e.g., Basic, Premium)
#     price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the plan
#     duration_in_days = models.IntegerField()  # Duration of the plan in days
#     description = models.TextField(blank=True, null=True)  # Plan details

#     def __str__(self):
#         return f"{self.plan_id} - {self.plan_name}"



# class Subscription(models.Model):
#     subscription_id = models.AutoField(primary_key=True)  # Primary key
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     user_role = models.CharField(max_length=50, blank=True, null=True)
#     subscription_plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
#     subscription_date = models.DateTimeField(auto_now_add=True)  # When the subscription was made
#     subscription_start_date = models.DateField(blank=True, null=True)
#     subscription_end_date = models.DateField(blank=True, null=True)

#     def __str__(self):
#         return f"{self.subscription_id}"


# models.py

from django.db import models
from users.models import User

# Choices for subscription plan user types
PLAN_USER_TYPE_CHOICES = (
    ('Agent', 'Agent'),
    ('Client', 'Client'),
)


class SubscriptionPlan(models.Model):
    plan_id = models.AutoField(primary_key=True)
    plan_name = models.CharField(max_length=100, unique=True)  # e.g., Sachet, Connect, Connect+, Relax
    description = models.TextField(blank=True, null=True)  # General plan description
    user_type = models.CharField(max_length=20, choices=PLAN_USER_TYPE_CHOICES)  # NEW FIELD

    def __str__(self):
        return f"{self.plan_name} ({self.user_type})"


class SubscriptionPlanVariant(models.Model):
    variant_id = models.AutoField(primary_key=True)
    plan_id = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE, related_name='variants')
    duration_in_days = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    contact_limit = models.IntegerField(null=True, blank=True)
    priority_support = models.BooleanField(default=False)
    instant_alerts = models.BooleanField(default=False)
    relationship_manager = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.plan_id.plan_name} - {self.duration_in_days} days"


from django.utils import timezone
from datetime import timedelta

class Subscription(models.Model):
    subscription_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription_variant = models.ForeignKey(SubscriptionPlanVariant, on_delete=models.CASCADE)
    subscription_status = models.CharField(max_length=40,null=True,blank=True)
    subscription_start_date = models.DateField(auto_now_add=True)
    subscription_end_date = models.DateField()

    def save(self, *args, **kwargs):
        if not self.subscription_start_date:
            self.subscription_start_date = timezone.now().date()
        if self.subscription_variant and self.subscription_start_date:
            self.subscription_end_date = self.subscription_start_date + timedelta(days=self.subscription_variant.duration_in_days)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.subscription_id} - {self.user_id.email}"
