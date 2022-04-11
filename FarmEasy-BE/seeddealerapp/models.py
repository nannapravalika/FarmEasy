from django.db import models

# Create your models here.
class SeedDealerModel(models.Model):
    seed_id=models.AutoField(primary_key=True)
    full_name=models.CharField(max_length=100,help_text='Enter First name')
    email=models.EmailField(max_length=100,help_text='Enter email')
    mobile=models.BigIntegerField()
    address=models.CharField(max_length=100)
    membership=models.CharField(max_length=100)
    licence_no=models.CharField(max_length=100,null=True)
    password=models.CharField(max_length=100,help_text='Enter Password')
    status=models.CharField(default="pending",max_length=100)
    class Meta:
        db_table='seed_dealer_details'
        
class SeedVarietiesModel(models.Model):
    variety_id=models.AutoField(primary_key=True)
    seed_id=models.IntegerField(null=True)
    variety_name=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    technical_name=models.CharField(max_length=100)
    crop_type=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)
    prize=models.IntegerField() 
    image=models.ImageField(upload_to='images/') 
    seed_yeid=models.CharField(max_length=100)
    plant_height=models.CharField(max_length=100)
    maturity=models.CharField(max_length=100)
    area=models.TextField()
    sold_by=models.CharField(max_length=100)
    
    class Meta:
        db_table='seed_varieties'
    
           
        
        