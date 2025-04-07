from django.db import models


class Commission(models.Model):
    commission_id = models.AutoField(primary_key=True)  # Primary key
    level_no = models.IntegerField()  # Level number (1 to 10)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)  # Commission percentage

    def __str__(self):
        return f"{self.commission_id}%"

# class Commission(models.Model):
#     commission_id = models.AutoField(primary_key=True)
#     transaction_id = models.CharField(max_length=150,blank=True, null=True)
#     partner_id = models.CharField(max_length=150,blank=True, null=True)
#     property_id = models.CharField(max_length=150,blank=True, null=True)
#     sale_price = models.CharField(max_length=150,blank=True, null=True)
#     commission_percentage = models.CharField(max_length=150,blank=True, null=True)
#     commission_amount = models.CharField(max_length=150,blank=True, null=True)
#     paid_commission_amount = models.CharField(max_length=150,blank=True, null=True)
#     balance_commission_amount = models.CharField(max_length=150,blank=True, null=True)
#     commission_payment_status = models.CharField(max_length=150,blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.commission_id}"
