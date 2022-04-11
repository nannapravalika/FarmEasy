from django.db import models

# Create your models here.
class SevamemberModel(models.Model):
    sevamember_id=models.AutoField(primary_key=True)
    full_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.BigIntegerField()
    password=models.CharField(max_length=100)
    
    class Meta:
        db_table='sevamember_details'