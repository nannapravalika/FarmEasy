from urllib import request
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from farmerapp.models import FarmerComplaintModel, FarmerFeedbackModel, FarmerHelpModel, FarmerModel
from fertilizerapp.models import FertilizerModel,AddFertilizerModel
from pesticidedealerapp.models import PesticideDealerModel,AddPesticideModels
from seeddealerapp.models import SeedDealerModel,SeedVarietiesModel
from machinerydealerapp.models import MachineryDealerModel,AddMachineryModel


# Create your views here.
def  farmerlogin(request):
    if request.method=="POST":
         
        email = request.POST.get('email')
        password =request.POST.get('password')
        
        try:
           check=FarmerModel.objects.get(email=email,password=password)
           request.session["farmer_id"]=check.farmer_id
           print('heloo')
           return redirect ('farmer_home')
        except: 
            pass
    return render(request,"farmer/farmerlogin.html")

def  farmer_registraion(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        aadhar=request.POST.get('aadhar')
        password=request.POST.get('password')
         
        
        FarmerModel.objects.create(full_name=fname,mobile=mobile,email=email,aadhar=aadhar,password=password)
        messages.success(request, "Message sent." )
    return render(request,"farmer/farmerregistration.html")

def  farmer_home(request):
    ferpcount=AddFertilizerModel.objects.count()
    pespcount=AddPesticideModels.objects.count()
    machpcount=AddMachineryModel.objects.count()
    seedpcount=SeedVarietiesModel.objects.count()
    pcount=ferpcount+pespcount+machpcount+seedpcount
    fcount=FarmerModel.objects.count()
    feedcount=FarmerFeedbackModel.objects.count()
    seeddcount=SeedDealerModel.objects.filter(status="accepted").count()
    ferdcount=FertilizerModel.objects.filter(status="accepted").count()
    pesdcount=PesticideDealerModel.objects.filter(status="accepted").count()
    machdcount=MachineryDealerModel.objects.filter(status="accepted").count()
    dcount=seeddcount+ferdcount+pesdcount+machdcount
    return render(request,"farmer/farmer-home.html",{'pcount':pcount,'fcount':fcount,'feedcount':feedcount,'dcount':dcount})

def  farmer_complaints(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        email=request.POST.get('email')
        city=request.POST.get('city') 
        complaint=request.POST.get('complaint')
        
        FarmerComplaintModel.objects.create(name=fname,email=email,complaint=complaint,city=city )
        messages.success(request, "Message sent." )
    return render(request,"farmer/farmer-complaints.html")

def  farmer_feedback(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        email=request.POST.get('email')
        city=request.POST.get('city')
        category=request.POST.get('category')
        feedback=request.POST.get('feedback')
        
        FarmerFeedbackModel.objects.create(name=fname,email=email,category=category,feedback=feedback,city=city)
        messages.success(request, "Message sent." )
    return render(request,"farmer/farmer-feedback.html")

def  farmer_help(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        city=request.POST.get('city')
        category=request.POST.get('category')
        passbook_No=request.POST.get('passbook_No')
        help=request.POST.get('help')
        
        FarmerHelpModel.objects.create(name=fname,mobile=mobile,email=email,category=category,passbook_No=passbook_No,city=city,help=help)
        messages.success(request, "Message sent." )
    return render(request,"farmer/farmer-help.html")

def  farmer_food_crops(request):
    return render(request,"farmer/food-crops.html")

def  farmer_non_food_crops(request):
    return render(request,"farmer/non-food-crops.html")

def  coffee(request):
    return render(request,"farmer/coffee-food.html")

def  maize(request):
    return render(request,"farmer/maize-food.html")

def  millets(request):
    return render(request,"farmer/millets-food.html")

def  oilseeds(request):
    return render(request,"farmer/oilseeds-food.html")

def  pulses(request):
    return render(request,"farmer/pulses-food.html")

def  rice(request):
    return render(request,"farmer/rice-food.html")

def  sugarcane(request):
    return render(request,"farmer/sugarcane-food.html")

def  tea(request):
    return render(request,"farmer/tea-food.html")

def  wheat(request):
    return render(request,"farmer/wheat-food.html")

def  rubber(request):
    return render(request,"farmer/rubber-non-food.html")

def  fibre(request):
    return render(request,"farmer/fibre-non-food.html")

#fertilizer 

def  farmer_fertilizer_dealers(request):
    dealers=FertilizerModel.objects.filter(status="accepted")
    return render(request,"farmer/farmer-fertilizer-dealers.html",{'d':dealers})

def fertilizer_dealer_varieties(request,id):
    detail=AddFertilizerModel.objects.filter(fertilizer_id=id)
    return render(request,"farmer/farmer-fertilizer.html",{'var':detail})

def  farmer_fertilizer(request):
    view=AddFertilizerModel.objects.all()
    return render(request,"farmer/farmer-fertilizer.html",{'var':view})

def farmer_fertilizer_detail(request,id):
    detail=AddFertilizerModel.objects.filter(product_id=id)
    return render(request,'farmer/farmer-fertilizer-details.html',{'D':detail})

def fertilizer_dealer(request,id):
    dealers=FertilizerModel.objects.filter(fertilizer_id=id)
    return render(request,"farmer/farmer-fertilizer-dealers.html",{'d':dealers})

#machinery

def  farmer_machinery_dealers(request):
    dealers=MachineryDealerModel.objects.filter(status="accepted")
    return render(request,"farmer/farmer-machinery-dealers.html",{'d':dealers})

def machinery_dealer_varieties(request,id):
    detail=AddMachineryModel.objects.filter(machinery_id=id)
    return render(request,"farmer/farmer-machinery.html",{'var':detail})


def  farmer_machinery(request):
    view=AddMachineryModel.objects.all()
    return render(request,"farmer/farmer-machinery.html",{'var':view})

def farmer_machinery_detail(request,id):
    detail=AddMachineryModel.objects.filter(product_id=id)
    return render(request,'farmer/farmer-machinery-details.html',{'D':detail})

def machinery_dealer(request,id):
    dealers=MachineryDealerModel.objects.filter(machinery_id=id)
    return render(request,"farmer/farmer-machinery-dealers.html",{'d':dealers})



#pesticide 

def  farmer_pesticide_dealers(request):
    dealers=PesticideDealerModel.objects.filter(status="accepted")
    return render(request,"farmer/farmer-pesticide-dealers.html",{'d':dealers})

def pesticide_dealer_varieties(request,id):
    detail=AddPesticideModels.objects.filter(pesticide_id=id)
    return render(request,"farmer/farmer-pesticide.html",{'var':detail})


def  farmer_pesticide(request):
    view=AddPesticideModels.objects.all()
    return render(request,"farmer/farmer-pesticide.html",{'var':view})

def farmer_pesticide_detail(request,id):
    detail=AddPesticideModels.objects.filter(product_id=id)
    return render(request,'farmer/farmer-pesticide-details.html',{'D':detail})

def pesticide_dealer(request,id):
    dealers=PesticideDealerModel.objects.filter(pesticide_id=id)
    return render(request,"farmer/farmer-pesticide-dealers.html",{'d':dealers})



#seed

def  farmer_seed_dealers(request):
    dealers=SeedDealerModel.objects.filter(status="accepted")
    return render(request,"farmer/farmer-seed-dealers.html",{'d':dealers})

def seed_dealer_varieties(request,id):
    detail=SeedVarietiesModel.objects.filter(seed_id=id)
    return render(request,"farmer/farmer-seed.html",{'var':detail})


def  farmer_seed(request):
    view=SeedVarietiesModel.objects.all()
    return render(request,"farmer/farmer-seed.html",{'var':view})
 

def farmer_seed_detail(request,id):
    detail=SeedVarietiesModel.objects.filter(variety_id=id)
    return render(request,'farmer/farmer-seed-details.html',{'D':detail})
 

def seed_dealer(request,id):
    dealers=SeedDealerModel.objects.filter(seed_id=id)
    return render(request,"farmer/farmer-seed-dealers.html",{'d':dealers})












    
    
    