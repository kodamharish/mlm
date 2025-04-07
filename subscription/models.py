from django.db import models
from users.models import *

# Create your models here.
class SubscriptionPlan(models.Model):
    plan_id = models.AutoField(primary_key=True)  # Primary key
    plan_name = models.CharField(max_length=100, unique=True)  # Plan name (e.g., Basic, Premium)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the plan
    duration_in_days = models.IntegerField()  # Duration of the plan in days
    description = models.TextField(blank=True, null=True)  # Plan details

    def __str__(self):
        return f"{self.plan_id} - {self.plan_name}"



class Subscription(models.Model):
    subscription_id = models.AutoField(primary_key=True)  # Primary key
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_role = models.CharField(max_length=50, blank=True, null=True)
    subscription_plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    subscription_date = models.DateTimeField(auto_now_add=True)  # When the subscription was made
    subscription_start_date = models.DateField(blank=True, null=True)
    subscription_end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.subscription_id}"
