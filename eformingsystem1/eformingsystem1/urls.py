"""eformingsystem1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from eformingsystem1 import settings
from app1 import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
path('',views.home,name="home"),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('welcome/',views.welcome,name='welcome'),
    path("open/",views.open,name="open"),
    path('Register/',views.register,name='Register'),
    path('changepassword/',views.chanegpassword,name='changepassword'),
    path('otpvalidation/',views.otpvalidation,name="otpvalidation"),
    path('pupdate/',views.update,name="pupdate"),
    path('change/',views.changeoldpassword,name='change'),
    path('otp/',views.changeoldpassword1,name='otp'),
    path('change1/',views.cahangedpassword2,name='change1'),
    path('changed/',views.chengedsuccessfully,name="changed"),
    path('addadmin/',views.addadmin,name="addadmin"),
    path('saveadmin/',views.saveadmin,name="saveadmin"),
    path('addagri/',views.addagricultureofficer,name="addagri"),
    path('saveofficer/',views.saveofficer,name="saveofficer"),
    path('scheme/',views.farmersscheme,name="scheme"),
    path('save_scheme/',views.save_scheme,name="save_scheme"),
    path('showschemes/',views.showscheme,name='showscheme'),
    path('insert_goods_price/',views.insert_goods_price,name="insert_goods_price"),
    path('savegoods/',views.savegoods,name="savegoods"),
    path('viewallofficer/',views.viewallofficer,name='viewallofficer'),
    path('update/',views.updateofficers,name='update'),
    path('savedupdatedata/',views.savedupdatedata,name="savedupdatedata"),
    path('delete/',views.deleteofficers,name='delete'),
    path('viewallgoodsprice/',views.viewallgoodsprice,name='viewallgoodsprice'),
    path('updategoods/',views.updategoods,name="updategoods"),
    path('updatedgoods/',views.updatedgoods,name='updatedgoods'),
    path('deletegoods/',views.deletegoods,name='deletegoods'),
    path('addtechno/',views.addtechno,name='addtechno'),
    path('uploadvideo/',views.uploadvideo,name='uploadvideo'),
    path('view_video/',views.view_video,name='view_video'),
    path('deletevideo/',views.deletevideo,name="deletevideo"),
    path('agriculturelogin/',views.agriculturelogin,name="agriculturelogin"),
    path('openofficer/',views.openofficer,name="openofficer"),
    path('validate/',views.validate,name="validate"),
    path('forgetoffice/',views.forgetoffice,name='forgetoffice'),
    path('reset/',views.reset,name='reset'),
    path('checkotp/',views.checkotp,name='checkotp'),
    path('updateofficer/',views.updateofficer,name='updateofficer'),
    path('changeoffpassword/',views.changeoffpassword,name='changeoffpassword'),
    path('ckeckotp2/',views.ckeckotp2,name='ckeckotp2'),
    path('otpckecking/',views.otpckecking,name='otpckecking'),
    path('updateofficer2/',views.updateofficer2,name='updateofficer2'),
    path('addsoil/',views.addsoil,name='addsoil'),
    path('savesoil/',views.savesoil,name="savesoil"),
    path('addcropinfo/',views.addcropinfo,name='addcropinfo'),
    path('savecrop/',views.savecrop,name='savecrop'),
    path('viewallsoil/',views.viewallsoil,name='viewallsoil'),
    path('viewallcrop/',views.viewallcrop,name='viewallcrop'),
    path('deletesoil/',views.deletesoil,name='deletesoil'),
    path('deletecrop/',views.deletecrop,name='deletecrop'),
    path('farmerslogin/',views.farmerslogin,name="farmerslogin"),
    path('farmersreg/',views.farmersregistration,name="farmersreg"),
    path('savefarmers/',views.savefarmers,name="savefarmers"),
    path('loginfarmes/',views.loginfarmes,name="loginfarmes"),
    path('openfarmer/',views.openfarmer,name="openfarmer"),
    path('farmesschems/',views.farmesschems,name="farmesschems"),
    path('farmesgoods/',views.farmesgoods,name="farmesgoods"),
    path('goodscat/',views.goodscat,name="goodscat"),
    path('farmesforget/',views.farmesforget,name="farmesforget"),
    path('farmerschange/',views.farmerschangepss,name="farmerschange"),
    path('fpasschanged/',views.fpasschanged,name='fpasschanged'),
    path('fquery/',views.fquery,name="fquery"),
    path('savequery/',views.savequery,name="savequery"),
    path('fviewvideo/',views.farmesvideo,name="fviewvideo"),
    path('fsoilinform/',views.fsoilinformation,name='fsoilinform'),
    path('fcropinfo/',views.fcropinformation,name="fcropinfo"),
    path('studentslog/',views.studentslogin,name="studentslog"),
    path('studwelcome/',views.studwelcome,name="studwelcome"),
    path('openstudent',views.openstudent,name="openstudent"),
    path('studentregi/',views.studentsregistration,name="studentregi"),
    path('studsave/',views.savestudents,name="studsave"),
    path('studforget/',views.studentsforget,name="studforget"),
    path('studconf/',views.studentsconf,name="studconf"),
    path('studpasschange/',views.studpasschange,name="studpasschange"),
    path('stdsoilinfo/',views.stdsoilinformation,name="stdsoilinfo"),
    path('studcropinf/',views.studcropinfo,name="studcropinf"),
    path('search/',views.search,name="search"),
    path('goods/',views.goodsprice,name="goods"),
    path('goodsprice/',views.goodpricenamewise,name="goodsprice"),
    path('stdquery/',views.studentsquery,name="stdquery"),
    path('stdviewsgoods/',views.stdviewsgoods,name="stdviewsgoods"),
    path('savestdqury/',views.savestdqury,name="savestdqury"),
    path('weather/',views.weather,name='weather'),
    path('weather1/',views.weather1,name='weather1'),
    path('admviewquery/',views.adminviewquery,name='admviewquery'),
    path('viewstdquery/',views.viewstdquery,name='viewstdquery'),
    path('reply',views.stdreply,name="reply"),
    path('sendquery/',views.sendquery,name="sendquery"),
    path('farmesquery/',views.farmesquery,name="farmesquery"),
    path('farmersreply/',views.farmersreply,name="farmersreply"),
    path('querysend/',views.querysend,name="querysend"),
    path('offiquerysave/',views.officerquerysave,name="offiquerysave"),
    path('officerqueryview/',views.officerqueryview,name="officerqueryview"),
    path('offreply/',views.offreply,name="offreply"),
    path('sendans/',views.sendans,name="sendans"),
    path('adlogout/',views.adminlogout,name="adlogout"),
    path('officerlogout/',views.officerlogout,name='officerlogout'),
    path('farmerlogout/',views.farmerlogout,name='farmerlogout'),
    path('studentslogout/',views.studentslogout,name='studentslogout')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

