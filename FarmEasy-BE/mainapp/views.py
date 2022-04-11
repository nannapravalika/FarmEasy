from contextlib import redirect_stderr
from django.shortcuts import render
from django.shortcuts import redirect, render
from adminapp.views import admin_home
from fertilizerapp.models import AddFertilizerModel,FertilizerModel
from machinerydealerapp.models import MachineryDealerModel,AddMachineryModel
from seeddealerapp.models import SeedDealerModel,SeedVarietiesModel
from farmerapp.models import FarmerFeedbackModel,FarmerModel
from pesticidedealerapp.models import PesticideDealerModel,AddPesticideModels
# Create your views here.
def index(request):
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
    
    return render(request,'main/index.html',{'pcount':pcount,'fcount':fcount,'feedcount':feedcount,'dcount':dcount})

def about(request):
    return render(request,'main/about.html')

def contact(request):
    return render(request,'main/contact.html')

def adminlogin (request):
    if request.method == "POST":
        name = request.POST.get('Username')
        password =request.POST.get('Password')
        if name =='admin' and password =='admin':
            return redirect (admin_home)
        else :
            print ('invalid')  
    return render (request,'main/adminlogin.html')

def majorcrops_index (request):
    return render (request,'main/major-crops-index.html')

def foodcrops_index (request):
    return render (request,'main/food-crops-index.html')

def nonfoodcrops_index (request):
    return render (request,'main/non-food-crops-index.html')