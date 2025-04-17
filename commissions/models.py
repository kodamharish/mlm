from django.db import models


class Commission(models.Model):
    commission_id = models.AutoField(primary_key=True)  # Primary key
    level_no = models.IntegerField()  # Level number (1 to 10)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)  # Commission percentage

    def __str__(self):
        return f"{self.commission_id}"


