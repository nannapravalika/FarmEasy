from django.db import models

# Create your models here.
class PesticideDealerModel(models.Model):
    pesticide_id=models.AutoField(primary_key=True)
    full_name=models.CharField(max_length=100,help_text='Enter First name')
    email=models.EmailField(max_length=100,help_text='Enter email')
    mobile=models.BigIntegerField()
    address=models.CharField(max_length=100)
    membership=models.CharField(max_length=100)
    licence_no=models.CharField(max_length=100,null=True)
    password=models.CharField(max_length=100,help_text='Enter Password')
    status=models.CharField(default="pending",max_length=100)
    class Meta:
        db_table='pesticide_dealer_details'
        
class AddPesticideModels(models.Model):
    product_id=models.AutoField(primary_key=True)
    pesticide_id=models.IntegerField(null=True)
    product_name=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    technical_name=models.CharField(max_length=100)
    type_of_pesticide=models.CharField(max_length=100)
    crop=models.TextField()
    diseases=models.TextField()
    dosage_per_ace=models.CharField(max_length=100)
    dialution_period=models.CharField(max_length=100)
    waiting_period=models.CharField(max_length=100)
    area_of_orgin=models.CharField(max_length=100)
    sold_by=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)
    prize=models.IntegerField() 
    image=models.ImageField(upload_to='images/') 
    benefits=models.TextField(null=True)
    desc=models.TextField()
    class Meta:
        db_table='pesticide_details'