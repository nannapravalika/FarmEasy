from unicodedata import category
from django.shortcuts import render,redirect
from django.contrib import messages
from fertilizerapp.models import FertilizerModel,AddFertilizerModel
from farmerapp.models import FarmerFeedbackModel,FarmerModel

# Create your views here.
def fertilizer_dealer_login(request):
    if request.method=="POST":
         
        email = request.POST.get('email')
        password =request.POST.get('password')
       
        try:
           check=FertilizerModel.objects.get(email=email,password=password)
           print("checked")
           request.session["fertilizer_id"]=check.fertilizer_id
           
           return redirect ('fertilizer_home')
        except: 
            pass
    return render(request,'fertilizer/Fertilizerlogin.html')

def fertilizer_reg(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        address=request.POST.get('address')
        membership=request.POST.get('membership')
        password=request.POST.get('password')
        license=request.POST.get('licence')
        
        FertilizerModel.objects.create(full_name=fname,mobile=mobile,email=email,address=address,membership=membership,password=password,licence_no=license)
        messages.success(request, "Message sent." )
    return render(request,'fertilizer/Fertilizer-reg.html')
    
def fertilizer_home(request):
    pcount=AddFertilizerModel.objects.count()
    fcount=FarmerModel.objects.count()
    feedcount=FarmerFeedbackModel.objects.filter(category="Fertilizer Dealer").count()
    return render(request,'fertilizer/fertilizer-home.html',{'pcount':pcount,'fcount':fcount,'feedcount':feedcount})

def fertilizer_add_varieties(request):
    fertilizer_id=request.session["fertilizer_id"]
    if request.method=="POST" and request.FILES ['image']:
        product_name=request.POST.get('product_name')
        company_name=request.POST.get('company_name')
        technical_name=request.POST.get('technical_name')
        type_of_fertilizer=request.POST.get('type_of_fertilizer')
        product_quality=request.POST.get('product_quality')
        benifits=request.POST.get('benifits')
        how_to_use=request.POST.get('how_to_use')
        area_of_orgin=request.POST.get('area_of_orgin')
        sold_by=request.POST.get('sold_by')
        quantity=request.POST.get('quantity')
        prize=request.POST.get('prize')
        image=request.FILES['image']
        
        AddFertilizerModel.objects.create(product_name=product_name,company_name=company_name,technical_name=technical_name,
                                          type_of_fertilizer=type_of_fertilizer,product_quality=product_quality,benifits=benifits,
                                          how_to_use=how_to_use,area_of_orgin=area_of_orgin,sold_by=sold_by,quantity=quantity,
                                          prize=prize,image=image,fertilizer_id=fertilizer_id)
        messages.success(request, "Message sent." )
    return render(request,'fertilizer/fertilizer-add-varieties.html')

def fertilizer_view_varieties(request):
    fer_id=request.session["fertilizer_id"]
    var=AddFertilizerModel.objects.filter(fertilizer_id=fer_id)
    return render(request,'fertilizer/fertilizer-view-varieties.html',{'var':var})

def fertilizer_varieties_details(request,id):
    detail=AddFertilizerModel.objects.filter(product_id=id)
    return render(request,'fertilizer/fertilizer-varieties-detail.html',{'D':detail})

def fertilizer_delete_variety(request,id):
    w = AddFertilizerModel.objects.filter(fertilizer_id=id)
    w.delete()
    return redirect('fertilizer_varieties_details')


def fertilizer_feedback(request):
    feed=FarmerFeedbackModel.objects.filter(category="Fertilizer Dealer")
    return render(request,'fertilizer/fertilizer-feedbacks.html',{'feed':feed})

    