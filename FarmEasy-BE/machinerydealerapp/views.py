from unicodedata import category
from django.shortcuts import render,redirect
from django.contrib import messages
from machinerydealerapp.models import MachineryDealerModel,AddMachineryModel
from farmerapp.models import FarmerFeedbackModel,FarmerModel

# Create your views here.
def machinery_dealer_login(request):
    if request.method=="POST":
         
        email = request.POST.get('email')
        password =request.POST.get('password')
        
        try:
           check=MachineryDealerModel.objects.get(email=email,password=password)
           request.session["machinery_id"]=check.machinery_id
           print('heloo')
           return redirect ('machinery_home')
        except: 
            pass
    return render(request,'machinery dealer/farm-machinery-login.html')

def machinery_reg(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        address=request.POST.get('address')
        membership=request.POST.get('membership')
        password=request.POST.get('password')
        license=request.POST.get('licence')
        
        MachineryDealerModel.objects.create(full_name=fname,mobile=mobile,email=email,address=address,membership=membership,password=password,licence_no=license)
        messages.success(request, "Message sent." )
    return render(request,'machinery dealer/farm-machinery-reg.html')
    
def machinery_home(request):
    pcount=AddMachineryModel.objects.count()
    fcount=FarmerModel.objects.count()
    feedcount=FarmerFeedbackModel.objects.filter(category="Machinery Dealer").count()
    return render(request,'machinery dealer/farm-machinery-home.html',{'pcount':pcount,'fcount':fcount,'feedcount':feedcount})

def machinery_add_varieties(request):
    machinery_id=request.session["machinery_id"]
    if request.method=="POST" and request.FILES['image']:
        product_name=request.POST.get('product_name')
        company_name=request.POST.get('company_name')
        machinery_type=request.POST.get('machinery_type')
        specifications=request.POST.get('specifications')
        function=request.POST.get('function')
        sold_by=request.POST.get('sold_by')
        prize=request.POST.get('prize')
        image=request.FILES['image']
        video=request.FILES['video']
        desc=request.POST.get('desc')
        AddMachineryModel.objects.create(product_name=product_name,company_name=company_name,machinery_type=machinery_type,
                                        specifications=specifications,function=function,sold_by=sold_by,prize=prize,
                                        image=image,video=video,desc=desc,machinery_id=machinery_id) 
        messages.success(request, "Message sent." )
    return render(request,'machinery dealer/farm-machinery-add-varieties.html')

def machinery_view_varieties(request):
    machinery_id=request.session["machinery_id"]
    var=AddMachineryModel.objects.filter(machinery_id=machinery_id)
    return render(request,'machinery dealer/farm-machinery-view-varieties.html',{'var':var})

def machinery_varieties_details(request,id):
    detail=AddMachineryModel.objects.filter(product_id=id)
    return render(request,'machinery dealer/farm-machinery-varieties-detail.html',{'D':detail})

def machinery_delete_variety(request,id):
    w = AddMachineryModel.objects.filter(machinery_id=id)
    w.delete()
    return redirect('machinery_varieties_details')



def machinery_feedback(request):
    feed=FarmerFeedbackModel.objects.filter(category="Machinery Dealer")
    return render(request,'machinery dealer/farm-machinery-feedbacks.html',{'feed':feed})

    