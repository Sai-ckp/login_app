from django.db import models

class StoreDetail(models.Model):
    store_name = models.CharField(max_length=100)
    remarks = models.CharField(max_length=100)
 
    def __str__(self):
        return self.store_name
