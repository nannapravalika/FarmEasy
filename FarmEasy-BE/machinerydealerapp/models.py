from django.db import models

# Create your models here.
class MachineryDealerModel(models.Model):
    machinery_id=models.AutoField(primary_key=True)
    full_name=models.CharField(max_length=100,help_text='Enter First name')
    email=models.EmailField(max_length=100,help_text='Enter email')
    mobile=models.BigIntegerField()
    address=models.CharField(max_length=100)
    membership=models.CharField(max_length=100)
    licence_no=models.CharField(max_length=100,null=True)
    password=models.CharField(max_length=100,help_text='Enter Password')
    status=models.CharField(default="pending",max_length=100)
    class Meta:
        db_table='machinery_dealer_details'
        
class AddMachineryModel(models.Model):
    product_id=models.AutoField(primary_key=True)
    machinery_id=models.IntegerField(null=True)
    product_name=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    machinery_type=models.CharField(max_length=100)
    specifications=models.TextField()
    function=models.TextField() 
    sold_by=models.CharField(max_length=100)
    prize=models.IntegerField() 
    image=models.ImageField(upload_to='images/') 
    video=models.FileField(upload_to='videos/')
    desc=models.TextField()     
    class Meta:
        db_table='machinery_details'  