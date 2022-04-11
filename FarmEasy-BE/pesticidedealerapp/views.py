import re
from unicodedata import category
from urllib import request
from django.shortcuts import render,redirect
from pesticidedealerapp.models import PesticideDealerModel,AddPesticideModels
from farmerapp.models import FarmerFeedbackModel,FarmerModel
from django.contrib import messages

# Create your views here.

def pesticide_dealer_login(request):
    if request.method=="POST":
         
        email = request.POST.get('email')
        password =request.POST.get('password')
        
        try:
           check=PesticideDealerModel.objects.get(email=email,password=password)
           request.session["pesticide_id"]=check.pesticide_id
           print('heloo')
           return redirect ('pesticide_home')
        except: 
            pass 
    return render(request,'pesticide/pesticide-dealer-login.html')

def pesticide_reg(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        address=request.POST.get('address')
        membership=request.POST.get('membership')
        password=request.POST.get('password')
        license=request.POST.get('licence')
        
        PesticideDealerModel.objects.create(full_name=fname,mobile=mobile,email=email,address=address,membership=membership,password=password,licence_no=license)
        messages.success(request, "Message sent." )
    return render(request,'pesticide/pesticide-reg.html')
    
def pesticide_home(request):
    pcount=AddPesticideModels.objects.count()
    fcount=FarmerModel.objects.count()
    feedcount=FarmerFeedbackModel.objects.filter(category="Pesticide Dealer").count()
    return render(request,'pesticide/pesticide-home.html',{'pcount':pcount,'fcount':fcount,'feedcount':feedcount})

def pesticide_add_varieties(request):
    pesticide_id=request.session["pesticide_id"]
    if request.method=="POST"and request.FILES['image']:
        product_name=request.POST.get('product_name')
        company_name=request.POST.get('company_name')
        technical_name=request.POST.get('technical_name')
        type_of_pesticide=request.POST.get('type_of_pesticide')
        crop=request.POST.get('crop')
        diseases=request.POST.get('diseases')
        dosage_per_ace=request.POST.get('dosage_per_ace')
        dialution_period=request.POST.get('dialution_period')
        waiting_period=request.POST.get('waiting_period')
        area_of_orgin=request.POST.get('area_of_orgin')
        sold_by=request.POST.get('sold_by')
        quantity=request.POST.get('quantity')
        prize=request.POST.get('prize')
        image=request.FILES['image']
        benefits=request.POST.get('benefits')
        desc=request.POST.get('desc')
        AddPesticideModels.objects.create(product_name=product_name,company_name=company_name,technical_name=technical_name,
                                          type_of_pesticide=type_of_pesticide,crop=crop,diseases=diseases,dosage_per_ace=dosage_per_ace,
                                          dialution_period=dialution_period,waiting_period=waiting_period,area_of_orgin=area_of_orgin,
                                          sold_by=sold_by,quantity=quantity,prize=prize,image=image,benefits=benefits,desc=desc,pesticide_id=pesticide_id)
        messages.success(request, "Message sent." )
    return render(request,'pesticide/pesticide-add-varieties.html')

def pesticide_view_varieties(request):
    pesticide_id=request.session["pesticide_id"]
    var=AddPesticideModels.objects.filter(pesticide_id=pesticide_id)
    return render(request,'pesticide/pesticide-view-varieties.html',{'var':var})

def pesticide_varieties_details(request,id):
    detail=AddPesticideModels.objects.filter(product_id=id)
    return render(request,'pesticide/pesticide-varieties-detail.html',{'D':detail})

def pesticide_delete_variety(request,id):
    w = AddPesticideModels.objects.filter(pesticide_id=id)
    w.delete()
    return redirect('pesticide_varieties_details')

def pesticide_feedback(request):
    feed=FarmerFeedbackModel.objects.filter(category="Pesticide Dealer")
    return render(request,'pesticide/pesticide-feedbacks.html',{'feed':feed})

    