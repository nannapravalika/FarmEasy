import email
from unicodedata import category
from django.shortcuts import render,redirect
 
from seeddealerapp.models  import SeedDealerModel,SeedVarietiesModel
from farmerapp.models import FarmerFeedbackModel,FarmerModel
from django.contrib import messages 



# Create your views here.
def  seed_dealer_login(request):
    if request.method=="POST":
         
        email = request.POST.get('email')
        password =request.POST.get('password')
        
        try:
           check=SeedDealerModel.objects.get(email=email,password=password)
           request.session["seed_id"]=check.seed_id
           print('heloo')
           return redirect ('seed_home')
        except: 
            pass 
    return render(request,'seed dealer/seed-dealer-login.html')

def seed_dealer_reg(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        address=request.POST.get('address')
        membership=request.POST.get('membership')
        password=request.POST.get('password')
        license=request.POST.get('licence')
        
        SeedDealerModel.objects.create(full_name=fname,mobile=mobile,email=email,address=address,membership=membership,password=password,licence_no=license)
        messages.success(request, "Message sent." )
        
    return render(request,'seed dealer/seed-dealer-reg.html')
    
def seed_dealer_home(request):
    pcount=SeedVarietiesModel.objects.count()
    fcount=FarmerModel.objects.count()
    feedcount=FarmerFeedbackModel.objects.filter(category="Seed Dealer").count()
    return render(request,'seed dealer/seed-dealer-home.html',{'pcount':pcount,'fcount':fcount,'feedcount':feedcount})

def seed_add_varieties(request):
    seed_id=request.session["seed_id"]
    if request.method=="POST" and request.FILES ['image']:
        variety_name=request.POST.get('variety_name')
        company_name=request.POST.get('company_name')
        crop_type=request.POST.get('crop_type')
        quantity=request.POST.get('quantity')
        prize=request.POST.get('prize')
        image=request.FILES['image']
        seed_yeid=request.POST.get('seed_yeid')
        plant_height=request.POST.get('plant_height')
        maturity=request.POST.get('maturity')
        area=request.POST.get('area')
        sold_by=request.POST.get('sold_by')
        technical_name=request.POST.get('technical_name')
        SeedVarietiesModel.objects.create(variety_name=variety_name,company_name=company_name,crop_type=crop_type,
                                          quantity=quantity,prize=prize,image=image,seed_yeid=seed_yeid,plant_height=plant_height,
                                          maturity=maturity,area=area,seed_id=seed_id,sold_by=sold_by,technical_name=technical_name)
        messages.success(request, "Message sent." )
    return render(request,'seed dealer/seed-add-varieties.html')

def seed_view_varieties(request):
    seed_id=request.session["seed_id"]
    var=SeedVarietiesModel.objects.filter(seed_id=seed_id)
    return render(request,'seed dealer/seed-view-varieties.html',{'var':var})

def seed_varieties_details(request,id):
    detail=SeedVarietiesModel.objects.filter(variety_id=id)
    return render(request,'seed dealer/seed-varieties-detail.html',{'D':detail})

def seed_delete_variety(request,id):
    w = SeedVarietiesModel.objects.filter(seed_id=id)
    w.delete()
    return redirect('seed_varieties_details')


def seed_feedback(request):
    feed=FarmerFeedbackModel.objects.filter(category="Seed Dealer")
    return render(request,'seed dealer/seed-feedbacks.html',{'feed':feed})

    