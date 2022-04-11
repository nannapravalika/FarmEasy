from importlib.resources import path
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from farmeasy.settings import DEFAULT_FROM_EMAIL

from adminapp.models import SevamemberModel
from farmerapp.models import FarmerComplaintModel,FarmerHelpModel,FarmerFeedbackModel,FarmerModel
from fertilizerapp.models import FertilizerModel
from pesticidedealerapp.models import PesticideDealerModel
from seeddealerapp.models import SeedDealerModel
from machinerydealerapp.models import MachineryDealerModel

# Create your views here.
def admin_home(request):
    fcount=FarmerModel.objects.count()
    feedcount=FarmerFeedbackModel.objects.count()
    ccount=FarmerComplaintModel.objects.count()
    fercount=FertilizerModel.objects.filter(status="accepted").count()
    pcount=PesticideDealerModel.objects.filter(status="accepted").count()
    seedcount=SeedDealerModel.objects.filter(status="accepted").count()
    sevacount=SevamemberModel.objects.count()
    machcount=MachineryDealerModel.objects.filter(status="accepted").count()
    return render(request,'admin/admin-home.html',{'fcount':fcount,'feedcount':feedcount,'ccount':ccount,'fercount':fercount,'pcount':pcount,'seedcount':seedcount,'sevacount':sevacount,'machcount':machcount})

def admin_complaints(request):
    req=FarmerComplaintModel.objects.all()
    return render(request,'admin/admin-complants.html',{'req':req})

def admin_farm_mach_req(request):
    req=MachineryDealerModel.objects.all()
    return render(request,'admin/admin-farm-mach-req.html',{'req':req})

def mach_accept(request,id):
    accept=get_object_or_404(MachineryDealerModel,machinery_id=id)
    accept.status='accepted'
    accept.save(update_fields=["status"])
    accept.save()
    
    #email code
    html_content = "<br/><p>Dealer Request Status :<strong> Accepted </strong> </p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [accept.email]
    # if send_mail(subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Dealer Status", html_content, from_mail, to_mail)
    msg.attach_alternative(html_content, "text/html")
    if msg.send():
        print("Sent")
    return redirect ("admin-machinery-req")
 
def mach_reject(request,id):
    accept=get_object_or_404(MachineryDealerModel,machinery_id=id)
    accept.status='rejected'
    accept.save(update_fields=["status"])
    accept.save() 
    return redirect ("admin-machinery-req")

def admin_farm_mach_view(request):
    req=MachineryDealerModel.objects.all()
    return render(request,'admin/admin-farm-mach-view.html',{'req':req})

def mach_remove(request,id):
    w = MachineryDealerModel.objects.filter(machinery_id=id)
    w.delete()
    return redirect('admin-machinery-view')

def admin_farmer_view(request):
    
    req=FarmerModel.objects.all()
    return render(request,'admin/admin-farmer-view.html',{'req':req})

def admin_feedback(request):
    
    req=FarmerFeedbackModel.objects.all()
    return render(request,'admin/admin-feedback.html',{'req':req})

def admin_fertilizer_req(request):
    
    req=FertilizerModel.objects.all()
    return render(request,'admin/admin-fertilizer-req.html',{'req':req})

def fertilizer_accept(request,id):
    accept=get_object_or_404(FertilizerModel,fertilizer_id=id)
    accept.status='accepted'
    accept.save(update_fields=["status"])
    accept.save()
    
    #email code
    html_content = "<br/><p>Dealer Request Status :<strong> Accepted </strong> </p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [accept.email]
    # if send_mail(subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Dealer Status", html_content, from_mail, to_mail)
    msg.attach_alternative(html_content, "text/html")
    if msg.send():
        print("Sent")
    return redirect ("admin-fertilizer-req")
 
def fertilizer_reject(request,id):
    accept=get_object_or_404(FertilizerModel,fertilizer_id=id)
    accept.status='rejected'
    accept.save(update_fields=["status"])
    accept.save() 
    return redirect ("admin-fertilizer-req")

def admin_fertilizer_view(request):
     
    req=FertilizerModel.objects.all()
    return render(request,'admin/admin-fertilizer-view.html',{'req':req})

def admin_pesticide_req(request):
    
    req=PesticideDealerModel.objects.all()
    return render(request,'admin/admin-pesticide-req.html',{'req':req})

def pesticide_accept(request,id):
    accept=get_object_or_404(PesticideDealerModel,pesticide_id=id)
    accept.status='accepted'
    accept.save(update_fields=["status"])
    accept.save()
    
    #email code
    html_content = "<br/><p>Dealer Request Status :<strong> Accepted </strong> </p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [accept.email]
    # if send_mail(subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Dealer Status", html_content, from_mail, to_mail)
    msg.attach_alternative(html_content, "text/html")
    if msg.send():
        print("Sent")
    return redirect ("admin-pesticide-req")
 
def pesticide_reject(request,id):
    accept=get_object_or_404(PesticideDealerModel,pesticide_id=id)
    accept.status='rejected'
    accept.save(update_fields=["status"])
    accept.save() 
    return redirect ("admin-pesticide-req")


def admin_pesticide_view(request):
     
    req=PesticideDealerModel.objects.all()
    return render(request,'admin/admin-pesticide-view.html',{'req':req})

def admin_seed_req(request):
    
    req=SeedDealerModel.objects.all()
    return render(request,'admin/admin-seed-req.html',{'req':req})

def seed_accept(request,id):
    accept=get_object_or_404(SeedDealerModel,seed_id=id)
    accept.status='accepted'
    accept.save(update_fields=["status"])
    accept.save()
    
    #email code
    html_content = "<br/><p>Dealer Request Status :<strong> Accepted </strong> </p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [accept.email]
    # if send_mail(subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Dealer Status", html_content, from_mail, to_mail)
    msg.attach_alternative(html_content, "text/html")
    if msg.send():
        print("Sent")
    return redirect ("admin-seed-req")
 
def seed_reject(request,id):
    accept=get_object_or_404(SeedDealerModel,seed_id=id)
    accept.status='rejected'
    accept.save(update_fields=["status"])
    accept.save() 
    return redirect ("admin-seed-req")

def admin_seed_view(request):
     
    req=SeedDealerModel.objects.all()
    return render(request,'admin/admin-view-seed-dealers.html',{'req':req })

def admin_sevamem_req(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        password=request.POST.get('password')
         
        
        SevamemberModel.objects.create(full_name=fname,mobile=mobile,email=email,password=password)
        messages.success(request, "Message sent." )
    return render(request,'admin/admin-sevamem-req.html')

def admin_sevamem_view(request):
    
    req=SevamemberModel.objects.all()
    return render(request,'admin/admin-sevamem-view.html',{'req':req})



