from django.db import models
from users.models import *
from property.models import *


# class Transaction(models.Model):
#     transaction_id = models.AutoField(primary_key=True)  # Primary key
#     property_id = models.ForeignKey("Property", on_delete=models.CASCADE)
#     agent_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     purchased_by = models.CharField(max_length=50, choices=[("user", "User"), ("agent", "Agent")])
#     purchased_type = models.CharField(max_length=50, choices=[("direct", "Direct"), ("mlm_office", "MLM Office")])
#     purchased_agent_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     username = models.CharField(max_length=150)  # Store username for record-keeping
#     amount = models.DecimalField(max_digits=15, decimal_places=2)  # Transaction amount
#     commission = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Agent commission
#     property_amount = models.DecimalField(max_digits=15, decimal_places=2)  # Property price
#     company_commission = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Company commission
#     transaction_date = models.DateTimeField(auto_now_add=True)  # Transaction timestamp

#     def __str__(self):
#         return f"Transaction {self.transaction_id} - {self.username} - {self.amount}"





class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)  # Primary key

    # Ensure Property model reference is correct
    property_id = models.ForeignKey(
        "property.Property",  # Update this to correct app label if needed
        on_delete=models.CASCADE
    )

    agent_id = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="agent_transactions"
    )

    purchased_by = models.CharField(
        max_length=50, choices=[("user", "User"), ("agent", "Agent")]
    )
    
    purchased_type = models.CharField(
        max_length=50, choices=[("direct", "Direct"), ("mlm_office", "MLM Office")]
    )
    
    purchased_agent_id = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="purchased_agent_transactions"
    )
    
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_transactions"
    )

    username = models.CharField(max_length=150)  # Store username for record-keeping
    amount = models.DecimalField(max_digits=15, decimal_places=2)  # Transaction amount
    commission = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Agent commission
    property_amount = models.DecimalField(max_digits=15, decimal_places=2)  # Property price
    company_commission = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Company commission
    transaction_date = models.DateTimeField(auto_now_add=True)  # Transaction timestamp

    def __str__(self):
        return f"Transaction {self.transaction_id} - {self.username} - {self.amount}"

