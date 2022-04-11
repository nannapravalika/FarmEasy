"""farmeasy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path

from adminapp import views as admin_views
from farmerapp import views as farmer_views
from fertilizerapp import views as fertilizer_views
from machinerydealerapp import views as machinerydealer_views
from seeddealerapp import views as seeddealer_views
from sevamemberapp import views as sevamember_views
from pesticidedealerapp import views as pesticidedealer_views
from mainapp import views as main_views




from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # main urls start
    path('',main_views.index,name='index'),
    path('about',main_views.about,name='about'),
    path('contact',main_views.contact,name='contact'),
    path('admin-login',main_views.adminlogin,name='adminlogin'),
    path('major-crops-index',main_views.majorcrops_index,name='major_crops_index'),
    path('non-foodcrops-index',main_views.nonfoodcrops_index,name='non-food-crops-index'),
    path('food-crops-index',main_views.foodcrops_index,name='food-crops-index'),
    #main urls end
    
    # admin urls start
    path('admin-home',admin_views.admin_home,name='admin-home'),
    path('admin-complaints',admin_views.admin_complaints,name='admin-complaints'),
    #admin-machinery
    path('admin-machinery-req',admin_views.admin_farm_mach_req,name='admin-machinery-req'),
    path('accept-req/<int:id>/',admin_views.mach_accept,name='accept-req'),
    path('reject-req/<int:id>/',admin_views.mach_reject,name='reject-req'),

    path('admin-machinery-view',admin_views.admin_farm_mach_view,name='admin-machinery-view'),
    path('mach-remove/<int:id>/',admin_views.mach_remove,name='mach-remove'),
    #admin-farmer
    path('admin-farmer-view',admin_views.admin_farmer_view,name='admin-farmer-view'),
    path('admin-feedback',admin_views.admin_feedback,name='admin-feedback'),
    #admin-fertilizer
    path('admin-fertilizer-req',admin_views.admin_fertilizer_req,name='admin-fertilizer-req'),
    path('fertilizer-accept-req/<int:id>/',admin_views.fertilizer_accept,name='fertilizer-accept-req'),
    path('fertilizer-reject-req/<int:id>/',admin_views.fertilizer_reject,name='fertilizer-reject-req'),
    
    path('admin-fertilizer-view',admin_views.admin_fertilizer_view,name='admin-fertilizer-view'),
    #admin-pesticide
    path('admin-pesticide-req',admin_views.admin_pesticide_req,name='admin-pesticide-req'),
    path('pesticide-accept-req/<int:id>/',admin_views.pesticide_accept,name='pesticide-accept-req'),
    path('pesticide-reject-req/<int:id>/',admin_views.pesticide_reject,name='pesticide-reject-req'),
    
    path('admin-pesticide-view',admin_views.admin_pesticide_view,name='admin-pesticide-view'),
    #admin-seed
    path('admin-seed-req',admin_views.admin_seed_req,name='admin-seed-req'),
    path('seed-accept-req/<int:id>/',admin_views.seed_accept,name='seed-accept-req'),
    path('seed-reject-req/<int:id>/',admin_views.seed_reject,name='seed-reject-req'),
    
    path('admin-seed-view',admin_views.admin_seed_view,name='admin-seed-view'),
    #admin-sevamem
    path('admin-sevamem-req',admin_views.admin_sevamem_req,name='admin-sevamem-req'),
    path('admin-sevamem-view',admin_views.admin_sevamem_view,name='admin-sevamem-view'),
    #admin-urls-end
    
    #farmer-urls-start
    
    path('farmer-login',farmer_views.farmerlogin,name='farmerlogin'),
    path('farmer-registraion',farmer_views.farmer_registraion,name='farmer_registraion'),
    path('farmer-home',farmer_views.farmer_home,name='farmer_home'),
    path('farmer-complaints',farmer_views.farmer_complaints,name='farmer_complaints'),
    path('farmer-feedback',farmer_views.farmer_feedback,name='farmer_feedback'),
    path('farmer-help',farmer_views.farmer_help,name='farmer_help'),
    path('about-coffee',farmer_views.coffee,name='coffee'),
    path('about-rice',farmer_views.rice,name='rice'),
    path('about-maize',farmer_views.maize,name='maize'), 
    path('about-millets',farmer_views.millets,name='millets'),
    path('about-tea',farmer_views.tea,name='tea'),
    path('about-pulses',farmer_views.pulses,name='pulses'), 
    path('about-oilseeds',farmer_views.oilseeds,name='oilseeds'),
    path('about-sugarcane',farmer_views.sugarcane,name='sugarcane'),
    path('about-wheat',farmer_views.wheat,name='wheat'),
    path('farmer-food-crops',farmer_views.farmer_food_crops,name='farmer_food_crops'),
    path('about-rubber',farmer_views.rubber,name='rubber'),
    path('about-fibre',farmer_views.fibre,name='fibre'),
    path('farmer-non-food-crops',farmer_views.farmer_non_food_crops,name='farmer_non_food_crops'),
    #farmer-fertilizer
    path('farmer-fertilzer-varities',farmer_views.farmer_fertilizer,name='farmer_fertilizer_varities'),
    path('farmer-fertilizer-detail-variety/<int:id>/',farmer_views.farmer_fertilizer_detail,name='farmer_fertilizer_detail'),
    path('farmer-fertilizer-dealers',farmer_views.farmer_fertilizer_dealers,name='farmer_fertilizer_dealers'),
    path('fertilizer-dealer/<int:id>/',farmer_views.fertilizer_dealer,name='fertilizer_dealer'),
    path('fertilizer-dealer-varieties/<int:id>/',farmer_views.fertilizer_dealer_varieties,name='fertilizer_dealer_varieties'),
    #farmer-pesticide
    path('farmer-pesticide-varities',farmer_views.farmer_pesticide,name='farmer_pesticide_varities'), 
    path('farmer-pesticide-detail-variety/<int:id>/',farmer_views.farmer_pesticide_detail,name='farmer_pesticide_detail'),
    path('farmer-pesticide-dealers',farmer_views.farmer_pesticide_dealers,name='farmer_pesticide_dealers'),
    path('pesticide-dealer/<int:id>/',farmer_views.pesticide_dealer,name='pesticide_dealer'),
    path('pesticide-dealer-varieties/<int:id>/',farmer_views.pesticide_dealer_varieties,name='pesticide_dealer_varieties'),
    #farmer-machinery
    path('farmer-machinery-varities',farmer_views.farmer_machinery,name='farmer_machinery_varities'),
    path('farmer-machinery-detail-variety/<int:id>/',farmer_views.farmer_machinery_detail,name='farmer_machinery_detail'),
    path('farmer-machinery-dealers',farmer_views.farmer_machinery_dealers,name='farmer_machinery_dealers'),
    path('machinery-dealer/<int:id>/',farmer_views.machinery_dealer,name='machinery_dealer'),
    path('machinery-dealer-varieties/<int:id>/',farmer_views.machinery_dealer_varieties,name='machinery_dealer_varieties'),
    #farmer-seed
    path('farmer-seed-varities',farmer_views.farmer_seed,name='farmer_seed_varities'),
    path('farmer-seed-detail-variety/<int:id>/',farmer_views.farmer_seed_detail,name='farmer_seed_detail'),
    path('farmer-seed-dealers',farmer_views.farmer_seed_dealers,name='farmer_seed_dealers'),
    path('seed-dealer/<int:id>/',farmer_views.seed_dealer,name='seed_dealer'),
    path('seed-dealer-varieties/<int:id>/',farmer_views.seed_dealer_varieties,name='seed_dealer_varieties'),
    
    #farmer urls end
    
    
    # fertilizer urls start
    path('fertilizer-dealer-login',fertilizer_views.fertilizer_dealer_login,name='fertilizer_dealer_login'),
    path('fertilizer-dealer-reg',fertilizer_views.fertilizer_reg,name='fertilize_dealer_reg'),
    path('fertilizer-add-varieties',fertilizer_views.fertilizer_add_varieties,name='fertilizer_add_varieties'),
    path('fertilizer-view-varieties',fertilizer_views.fertilizer_view_varieties,name='fertilizer_view_varieties'),
    path('fertilizer-detail-variety/<int:id>/',fertilizer_views.fertilizer_varieties_details,name='fertilizer_varieties_details'),
    path('fertilizer-delete-variety/<int:id/',fertilizer_views.fertilizer_delete_variety,name='fertilizer_delete_variety'),
    path('fertilizer-home',fertilizer_views.fertilizer_home,name='fertilizer_home'),
    path('fertilizer-feedbacks',fertilizer_views.fertilizer_feedback,name='fertilizer_feedbacks'),
    # fertilizer urls end
    
    #pesticide urls start
    path('pesticide-dealer-login',pesticidedealer_views.pesticide_dealer_login,name='pesticide_dealer_login'),
    path('pesticide-dealer-reg',pesticidedealer_views.pesticide_reg,name='pesticide_dealer_reg'),
    path('pesticide-add-varieties',pesticidedealer_views.pesticide_add_varieties,name='pesticide_add_varieties'),
    path('pesticide-view-varieties',pesticidedealer_views.pesticide_view_varieties,name='pesticide_view_varieties'),
    path('pesticide-detail-variety/<int:id>/',pesticidedealer_views.pesticide_varieties_details,name='pesticide_varieties_details'),
    path('pesticide-delete-variety/<int:id/',pesticidedealer_views.pesticide_delete_variety,name='pesticide_delete_variety'),
    path('pesticide-home',pesticidedealer_views.pesticide_home,name='pesticide_home'),
    path('pesticide-feedbacks',pesticidedealer_views.pesticide_feedback,name='pesticide_feedbacks'),
    #pesticide urls end
    
    #seed urls start
    path('seed-dealer-login',seeddealer_views.seed_dealer_login,name='seed_dealer_login'),
    path('seed-dealer-reg',seeddealer_views.seed_dealer_reg,name='seed_dealer_reg'),
    path('seed-add-varieties',seeddealer_views.seed_add_varieties,name='seed_add_varieties'),
    path('seed-view-varieties',seeddealer_views.seed_view_varieties,name='seed_view_varieties'),
    path('seed-detail-variety/<int:id>/',seeddealer_views.seed_varieties_details,name='seed_varieties_details'),
    path('seed-delete-variety/<int:id/',seeddealer_views.seed_delete_variety,name='seed_delete_variety'),
    path('seed-home',seeddealer_views.seed_dealer_home,name='seed_home'),
    path('seed-feedbacks',seeddealer_views.seed_feedback,name='seed_feedbacks'),
    #seed urls end

    #machinery urls start
    path('machinery-dealer-login',machinerydealer_views.machinery_dealer_login,name='machinery_dealer_login'),
    path('machinery-dealer-reg',machinerydealer_views.machinery_reg,name='machinery_dealer_reg'),
    path('machinery-add-varieties',machinerydealer_views.machinery_add_varieties,name='machinery_add_varieties'),
    path('machinery-view-varieties',machinerydealer_views.machinery_view_varieties,name='machinery_view_varieties'),
    path('machinery-detail-variety/<int:id>/',machinerydealer_views.machinery_varieties_details,name='machinery_varieties_details'),
    path('machinery-delete-variety/<int:id/',machinerydealer_views.machinery_delete_variety,name='machinery_delete_variety'), 
    path('machinery-home',machinerydealer_views.machinery_home,name='machinery_home'),
    path('machinery-feedbacks',machinerydealer_views.machinery_feedback,name='machinery_feedbacks'),
     #machinery urls end
    
    #sevamember urls start
    path('sevamember-login',sevamember_views.sevamember_login,name='sevamember_login'),
    path('sevamember-home',sevamember_views.sevamember_home,name='sevamember_home'),
    path('sevamember-requests',sevamember_views.sevamember_requests,name='sevamember_requests'),
    path('sevamember-reply/<int:id>/',sevamember_views.sevamember_reply,name='sevamember_reply'),
    path('submit-reply',sevamember_views.reply_send,name='submit-reply'),
    path('sevamember-feedback',sevamember_views.sevamember_feedback,name='sevamember_feedbacks'),
    #sevamember urls end
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)