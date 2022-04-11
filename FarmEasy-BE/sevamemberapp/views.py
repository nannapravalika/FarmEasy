from unicodedata import category
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from farmeasy.settings import DEFAULT_FROM_EMAIL
from adminapp.models import SevamemberModel
from farmerapp.models import FarmerHelpModel,FarmerFeedbackModel,FarmerModel

# Create your views here.
def  sevamember_login(request):
    if request.method=="POST":
         
        email = request.POST.get('email')
        password =request.POST.get('password')
        
        try:
           check=SevamemberModel.objects.get(email=email,password=password)
           request.session["seva_id"]=check.sevamember_id
           print('heloo')
           return redirect ('sevamember_home')
        except: 
            pass
    return render(request,'sevamember/sevamember-login.html')
    
def sevamember_home(request):
    hcount=FarmerHelpModel.objects.count()
    rcount=FarmerHelpModel.objects.filter(status="replied").count()
    fcount=FarmerModel.objects.count()
    feedcount=FarmerFeedbackModel.objects.filter(category="Website Administrative").count()
    return render(request,'sevamember/sevamember-home.html',{'hcount':hcount,'rcount':rcount,'fcount':fcount,'feedcount':feedcount})

def sevamember_requests(request):
    req=FarmerHelpModel.objects.all()
    return render(request,'sevamember/sevamember-requests.html',{'req':req})

def sevamember_reply(request,id):
    help=FarmerHelpModel.objects.filter(help_id=id)
    if request.method=="POST":
        reply=request.POST.get("reply")
        
        send=get_object_or_404(FarmerHelpModel,help_id=id)
        send.status="replied"
        send.reply=reply
        send.save(update_fields=["status","reply"])
        send.save()
        
        
     #email code
        html_content = "<br/><p>Help Request Reply :<strong>" + str(reply) + "</strong> </p>"
        from_mail = DEFAULT_FROM_EMAIL
        to_mail = [send.email]
        # if send_mail(subject,message,from_mail,to_mail):
        msg = EmailMultiAlternatives("Dealer Status", html_content, from_mail, to_mail)
        msg.attach_alternative(html_content, "text/html")
        if msg.send():
            print("Sent")
            
        messages.success(request, "Message sent." )    
    return render(request,'sevamember/sevamember-reply.html',{'help':help})

def reply_send(request):
    
    if request.method=="POST":
        print("ok")
        reply=request.POST.get('reply')
        
        FarmerHelpModel.objects.create(reply=reply)
        
        
        
       
    return redirect ('sevamember_reply')
def sevamember_feedback(request):
    feed=FarmerFeedbackModel.objects.filter(category="Website Administrative")
    return render(request,'sevamember/sevamember-feedbacks.html',{'feed':feed})

    