import email
from unicodedata import category, name
from django.db import models

# Create your models here.
class FarmerModel(models.Model):
    farmer_id=models.AutoField(primary_key=True)
    full_name=models.CharField(max_length=100,help_text='Enter First name')
    email=models.EmailField(max_length=100,help_text='Enter email')
    mobile=models.BigIntegerField()
    aadhar=models.BigIntegerField()
    password=models.CharField(max_length=100,help_text='Enter Password')
    
    class Meta:
        db_table='farmer_details'
        
class FarmerFeedbackModel(models.Model):
    feedback_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100) 
    email=models.EmailField(max_length=100) 
    city=models.CharField(max_length=100) 
    category=models.CharField(max_length=100) 
    feedback=models.TextField()  
    
    class Meta:
        db_table='farmer_feedback_details'      

class FarmerComplaintModel(models.Model):
    complaint_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100) 
    email=models.EmailField(max_length=100) 
    city=models.CharField(max_length=100) 
    complaint=models.TextField()   
    
    class Meta:
        db_table="farmer_complaint_details"   

class FarmerHelpModel(models.Model):
    help_id=models.AutoField(primary_key=100)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.BigIntegerField()
    city=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    passbook_No=models.BigIntegerField()
    help=models.TextField(max_length=100) 
    reply=models.TextField()            
    status=models.CharField(max_length=100,default="pending",null=True)
    
    class Meta:
        db_table="farmer_help_details"