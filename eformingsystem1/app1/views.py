from django.shortcuts import render,redirect
from django.contrib.sessions.models import Session
from django.core.paginator import Paginator
from eformingsystem1 import settings as se
from django.core.mail import send_mail
from app1.models import admin
from app1.models import otp
from app1.models import agricultureofficers
from app1.models import schememodel
from app1.models import goodspricemodule
from app1.models import uplaodvideomodel,soilinformation,cropinformation,farmersmodel,Query,StudentsModel,studentsQuery,oficersquerymodel
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponse
def home(request):
    return render(request,"home.html")


def adminlogin(request):
    return render(request,"adminlogin.html")

def welcome(request):
    try:
        email = request.POST["t1"]
        pas = request.POST["t2"]
        all = admin.objects.get(email=email, password=pas)
        request.session["email"] = all.email
        return redirect("open")
    except admin.DoesNotExist:
      message="please enter the correct username and password"
      return render(request, "adminlogin.html",{"message":message})

def open(request):
    return render(request,"welcome.html")

def register(request):
    return render(request,"Registar.html")

def chanegpassword(request):
    all=admin.objects.all()
    a=otp.objects.all()
    email=request.POST["t1"]
    name=request.POST["t2"]
    for x in all:
        if ((x.name==name) and (x.email==email)):
            import random
            otp2 = random.randint(100000, 999999)
            #otp(otp1=otp2).save()
            k = otp.objects.filter(id=1)
            k.update(otp1=otp2)
            sub = "this is otp"
            mess = "hello word""  " + str(otp2)
            send_mail(sub, mess, se.EMAIL_HOST_USER, [email])
            return render(request, "forgetpassword.html", {"message": "hello i sharanbasappa"})
        else:
            return render(request,"Registar.html",{"data":"invalid email and name"})


def otpvalidation(request):
    all=otp.objects.all()
    ss=request.POST["t1"]
    print(type(ss))
    print(ss)
    print(type(ss))
    for x in all:
      if str(x.otp1)==str(ss):
       return render(request,"otpvalidation.html",{"data":all})
      else:
        return render(request,'forgetpassword.html')


def update(request):
    all=admin.objects.all()
    name=request.POST["t1"]
    email1=request.POST["t2"]
    password=request.POST["t3"]
    conform=request.POST["t4"]
    for x in all:
        if x.email==email1 and x.name==name and conform==password:
            res = admin.objects.filter(email=email1)
            res.update(name=name,email=email1,password=password)
            return render(request,"otpvalidation.html",{"message":"password change successful"})
        else:
            return render(request,"otpvalidation.html",{"message":"this user name not avialable"})


def changeoldpassword(request):
    return render(request,"changeoldpassword.html")


def changeoldpassword1(request):
    all=admin.objects.all()
    email=request.POST["t1"]
    password=request.POST["t2"]
    for x in all:
        if x.email==email and x.password==password:
            import random
            otp2 = random.randint(100000, 999999)
            k = otp.objects.filter(id=1)
            k.update(otp1=otp2)
            sub = "this is otp"
            mess = "hello word""  " + str(otp2)
            send_mail(sub, mess, se.EMAIL_HOST_USER, [email])
            return render(request,"changepasswordotp.html")
        else:
          return render(request,"changeoldpassword.html")


def cahangedpassword2(request):
    all=admin.objects.all()
    a=otp.objects.all()
    otp2=request.POST["t1"]
    for x in a:
        if str(x.otp1)==otp2:
            return render(request,"setnewpassword.html")
        else:
            return render(request,"changepasswordotp.html",{"data":"plase enter correct otp"})


def chengedsuccessfully(request):
    all=admin.objects.all()
    email=request.POST["t1"]
    password=request.POST["t2"]
    newpassword=request.POST["t3"]
    for x in all:
        if x.email==email and x.password==password:
            res = admin.objects.filter(email=email)
            res.update( password=newpassword)
            return render(request,"setnewpassword.html",{"message":"changed password successfully"})
        else:
            return render(request,"setnewpassword.html",{"message1":"please enter the correct user name and password"})


def addadmin(request):
    res=request.session.get("email")
    if res:
      return render(request,"addadmin.html")
    else:
        return redirect("adminlogin")

def saveadmin(request):
    email=request.POST["t1"]
    name=request.POST["t2"]
    print(email)
    print(name)

    try:
      admin(email=email, password=name, name=name).save()
      sub = "hi this efarmers wesite "
      mess = "password=""  " +name+" "  "username=" +email
      send_mail(sub, mess,se.EMAIL_HOST_USER,[email])
      return render(request,"addadmin.html")
    except IntegrityError:
        return render(request,"addadmin.html",{"data":"this email aready available"})


def addagricultureofficer(request):
    res = request.session.get("email")
    if res:
        return render(request, "addagriculture.html")
    else:
        return redirect("adminlogin")



def saveofficer(request):
    idno=request.POST["t1"]
    name=request.POST["t2"]
    email=request.POST["t3"]
    profession=request.POST["t4"]
    expertise=request.POST["t5"]
    all=agricultureofficers.objects.all()
    for x in all:
        if x.idno==idno and x.email==email:
         return render(request,"addagriculture.html",{"data":"this idno and email id already available"})
    else:
        try:
          agricultureofficers(idno=idno,name=name,email=email,password=name,profession=profession,expertise=expertise).save()
          sub = "hi this efarmers wesite "
          mess = "password=""  " + name + " "  "username=" + email
          send_mail(sub, mess, se.EMAIL_HOST_USER, [email])
          return render(request,"addagriculture.html",{"data1":"data saved"})
        except IntegrityError:
            return render(request,"addagriculture.html",{"data":"this idno and email id already available"})


def farmersscheme(request):
    res = request.session.get("email")
    if res:
        return render(request, "uploadscheme.html")
    else:
        return redirect("adminlogin")



def save_scheme(request):
    name=request.POST["t1"]
    des=request.POST["t2"]
    schememodel(schemename=name,schemedes=des).save()
    return render(request,"uploadscheme.html",{"data":"data saved"})


def showscheme(request):
    all=schememodel.objects.all()
    return render(request,"showscheme.html",{"data":all})


def insert_goods_price(request):
    res = request.session.get("email")
    if res:
        return render(request, "insert_goods_price.html")
    else:
        return redirect("adminlogin")


def savegoods(request):
    name=request.POST["t1"]
    price=request.POST["t2"]
    quantity=request.POST["t3"]
    category=request.POST["t4"]
    image=request.FILES["t5"]
    try:
     goodspricemodule(goodsname=name,goodsprice=price,goodsquantity=quantity,category=category,goodsphoto=image).save()
     return render(request,"insert_goods_price.html",{"data":"data saved"})
    except IntegrityError:
        return render(request,"insert_goods_price.html",{"data1":name+"  ""already available"})


def viewallofficer(request):
    res = request.session.get("email")
    if res:
        all = agricultureofficers.objects.all()
        return render(request, "viewallofficer.html", {"data": all})
    else:
        return redirect("adminlogin")



def updateofficers(request):
    id = request.POST["t1"]
    res = agricultureofficers.objects.filter(idno=id)
    return render(request,"updateofficer.html",{"data":res})


def savedupdatedata(request):
    i=request.POST["t1"]
    n=request.POST["t2"]
    e=request.POST["t3"]
    pr=request.POST["t4"]
    ex=request.POST["t5"]
    res = agricultureofficers.objects.filter(idno=i)
    res.update(idno=i,name=n,email=e,profession=pr,expertise=ex)
    all=agricultureofficers.objects.all()
    return render(request,"viewallofficer.html",{"data":all})


def deleteofficers(request):
    id = request.POST["t1"]
    agricultureofficers.objects.filter(idno=id).delete()
    all = agricultureofficers.objects.all()
    return render(request,"viewallofficer.html",{"data":all})


def viewallgoodsprice(request):
    res = request.session.get("email")
    if res:
        all = goodspricemodule.objects.all()
        paginate = Paginator(all, 5)
        ps = request.GET.get("page_no", 1)
        obj = paginate.page(ps)
        return render(request, "allgoodsprice.html", {"data": obj})
    else:
        return redirect("adminlogin")




def updategoods(request):
    id = request.POST["t1"]
    res = goodspricemodule.objects.filter(goodsname=id)
    return render(request,"updategoods.html",{"data":res})


def updatedgoods(request):
    n = request.POST["t1"]
    p = request.POST["t2"]
    q = request.POST["t3"]
    c = request.POST["t4"]
    res = goodspricemodule.objects.filter(goodsname=n)
    res.update(goodsname=n,goodsprice=p,goodsquantity=q,category=c)
    all=goodspricemodule.objects.all()
    return render(request,"allgoodsprice.html",{"data":all})


def deletegoods(request):
    g = request.POST["t2"]
    goodspricemodule.objects.filter(goodsname=g).delete()
    all = goodspricemodule.objects.all()
    return render(request,"allgoodsprice.html",{"data":all})


def addtechno(request):
    res = request.session.get("email")
    if res:
        return render(request, "addtechno.html")
    else:
        return redirect("adminlogin")


def uploadvideo(request):
    n=request.POST["t1"]
    vi=request.FILES["t2"]
    des=request.POST["t3"]
    uplaodvideomodel(name=n,video=vi,description=des).save()
    return render(request,"addtechno.html",{"message":" upload successfully"})


def view_video(request):
    all=uplaodvideomodel.objects.all()
    return render(request,"view_video.html",{"data":all})


def deletevideo(request):
    ss= request.POST["t1"]
    uplaodvideomodel.objects.filter(name=ss).delete()
    all=uplaodvideomodel.objects.all()
    #aa=messages.SUCCESS(request,"delete your video")
    return render(request,"view_video.html",{"data":all})


def agriculturelogin(request):
    return render(request,"agriculturelogin.html")

def openofficer(request):
    return render(request,"welcomeofficerloginpage.html")
def validate(request):
    try:
        email = request.POST["t1"]
        pas = request.POST["t2"]
        all = agricultureofficers.objects.get(email=email, password=pas)
        request.session["email"] = all.email
        return redirect("openofficer")
    except agricultureofficers.DoesNotExist:
      message="please enter the correct username and password"
      return render(request, "agriculturelogin.html",{"message":message})


def forgetoffice(request):
    return render(request,"forgetofficerpassword.html")


def reset(request):
    all=agricultureofficers.objects.all()
    em=request.POST["t1"]
    i=request.POST["t2"]
    ii=int(i)
    for x in all:
        if ((x.idno == ii) and (x.email == em)):
            import random
            otp2 = random.randint(100000, 999999)
            #otp(otp1=otp2).save()
            k = otp.objects.filter(id=1)
            k.update(otp1=otp2)
            sub = "this is otp"
            mess = "hello word""  " + str(otp2)
            send_mail(sub, mess, se.EMAIL_HOST_USER, [em])
            return render(request,"setofficerpassword.html")
        else:
         return render(request,"forgetofficerpassword.html",{"data":"inavlid email or idno"})


def checkotp(request):
    all=otp.objects.all()
    ot=request.POST["t1"]
    ott=int(ot)
    for x in all:
        if x.otp1==ott:
          return render(request,"resetofficerpassword.html")
    return render(request,"setofficerpassword.html",{"message":"invalid otp"})


def updateofficer(request):
    all=agricultureofficers.objects.all()
    e=request.POST["t1"]
    p=request.POST["t2"]
    cp=request.POST["t3"]
    for x in all:
        if x.email==e and cp==p:
            res = agricultureofficers.objects.filter(email=e)
            res.update(email=e,password=p)
            return render(request,"resetofficerpassword.html",{"data":"change password successfully"})
        else:
            return render(request,"resetofficerpassword.html",{"data1":"invalid password or email"})


def changeoffpassword(request):
    return render(request,"changeoffpassword.html")


def ckeckotp2(request):
    email=request.POST["t1"]
    p=request.POST["t2"]
    all=agricultureofficers.objects.all()
    for x in all:
        if x.email==email and x.password==p:
            import random
            otp2 = random.randint(100000, 999999)
            # otp(otp1=otp2).save()
            k = otp.objects.filter(id=1)
            k.update(otp1=otp2)
            sub = "this is otp"
            mess = "hello word""  " + str(otp2)
            send_mail(sub, mess, se.EMAIL_HOST_USER, [email])
            return render(request,"checkotp2.html",{"data":all})
        else:
            return render(request,"changeoffpassword.html")


def otpckecking(request):
    all=otp.objects.all()
    ot = request.POST["t3"]
    ott = int(ot)
    for x in all:
        if x.otp1 == ott:
            return render(request,"updateofficers2.html")
    render(request,"changeoffpassword.html",{"message":"invalid otp"})


def updateofficer2(request):
    all = agricultureofficers.objects.all()
    e = request.POST["t1"]
    p = request.POST["t2"]
    cp = request.POST["t3"]
    for x in all:
        if x.email == e and cp == p:
            res = agricultureofficers.objects.filter(email=e)
            res.update(email=e, password=p)
            return render(request,"updateofficers2.html",{"data":"update successfulyy"})
    return render(request,"updateofficers2.html",{"data1":"not match password try again"})


def addsoil(request):
    res = request.session.get("email")
    if res:
        return render(request, "addsoil.html")
    else:
        return redirect("agriculturelogin")

def savesoil(request):
    try:
     n=request.POST["t1"]
     s=request.POST["t2"]
     r=request.POST["t3"]
     l=request.POST["t4"]
     cr=request.POST["t5"]
     i=request.FILES["t6"]
     soilinformation(name=n,state=s,rich=r,lacks=l,crops=cr,simage=i).save()
     return render(request,"addsoil.html",{"message":"saved"})
    except IntegrityError:
        return render(request,"addsoil.html",{"message1":"this name soil already available"})


def addcropinfo(request):
    res = request.session.get("email")
    if res:
        return render(request, "addcropinfo.html")
    else:
        return redirect("agriculturelogin")



def savecrop(request):
    try:
        n = request.POST["t1"]
        ty = request.POST["t2"]
        tem = request.POST["t3"]
        sty = request.POST["t4"]
        mpro = request.POST["t5"]
        hp = request.POST["t6"]
        hpc = request.POST["t7"]
        v = request.POST["t8"]
        r = request.POST["t9"]
        i = request.FILES["t10"]
        cropinformation(name=n, croptype=ty, temp=tem, soiltype=sty, majorpro=mpro, highpro=hp, highprocountry=hpc,
                        cropverities=v, rain=r, cropimage=i).save()
        return render(request, "addcropinfo.html", {"message": "crop saved"})
    except IntegrityError:
        return render(request,"addcropinfo.html",{"message1":"this crop information already available"})


def viewallsoil(request):
    res = request.session.get("email")
    if res:
        all = soilinformation.objects.all()
        return render(request, "viewallsoil.html", {"data": all})
    else:
        return redirect("agriculturelogin")



def viewallcrop(request):
    res = request.session.get("email")
    if res:
        all = cropinformation.objects.all()
        return render(request, "viewallcrop.html", {"data": all})
    else:
        return redirect("agriculturelogin")




def deletesoil(request):
    ss=request.POST['t1']
    all=soilinformation.objects.all()
    soilinformation.objects.filter(name=ss).delete()
    all = soilinformation.objects.all()
    return render(request,"viewallsoil.html",{"data":all})


def deletecrop(request):
    ss = request.POST['t1']
    cropinformation.objects.filter(name=ss).delete()
    all = cropinformation.objects.all()
    return render(request,"viewallcrop.html",{"data": all})


def farmerslogin(request):
    return render(request,"farmerslogin.html")


def farmersregistration(request):
    return render(request,"farmersregistartionform.html")


def savefarmers(request):
    try:
      name=request.POST["t1"]
      password=request.POST["t2"]
      adharno=request.POST["t3"]
      farmersmodel(name=name,password=password,adharno=adharno).save()
      return render(request,"farmersregistartionform.html",{"message":"Registration successful"})
    except IntegrityError:
        return render(request, "farmersregistartionform.html", {"message": "this farmers already exist "})


def loginfarmes(request):
 try:
        name = request.POST["t1"]
        pas = request.POST["t2"]
        all = farmersmodel.objects.get(name=name, password=pas)
        request.session["adharno"] = all.adharno
        return redirect("openfarmer")
 except farmersmodel.DoesNotExist:
      message="please enter the correct username and password"
      return render(request, "farmerslogin.html", {"message": "invalid user name and password"})

def openfarmer(request):
    return render(request,"farmerswelcom.html")


def farmesschems(request):
    res = request.session.get("adharno")
    if res:
        data = schememodel.objects.all()
        return render(request, "farmesschems.html", {"data": data})
    else:
        return redirect("agriculturelogin")



def farmesgoods(request):
    res = request.session.get("adharno")
    if res:
        data = goodspricemodule.objects.all()
        return render(request, "farmesgoodprice.html", {"data": data})
    else:
        return redirect("agriculturelogin")




def goodscat(request):
    res = request.session.get("adharno")
    if res:
        cat = request.GET["cate"]
        qs = goodspricemodule.objects.filter(category=cat)
        return render(request, "goodscatagery.html", {"data": qs})
    else:
        return redirect("agriculturelogin")


def farmesforget(request):
    return render(request,"farmesforget.html")


def farmerschangepss(request):
    name=request.POST["t1"]
    adhara=request.POST["t2"]
    all=farmersmodel.objects.all()
    for x in all:
        if name==x.name and int(adhara)==x.adharno:
            return render(request,"cahngefarmespassword.html")
    return render(request, "farmesforget.html",{"message":"invalid username and adhar number"})


def fpasschanged(request):
    name=request.POST["t1"]
    adh=request.POST["t2"]
    passw=request.POST["t3"]
    conf=request.POST["t4"]
    all=farmersmodel.objects.all()
    for x in all:
        if name==x.name and int(adh)==x.adharno and passw==conf:
             res=farmersmodel.objects.filter(adharno=adh)
             res.update(password=passw)
             return render(request,"cahngefarmespassword.html",{"message":"changed successfully"})
        else:
            return render(request, "cahngefarmespassword.html", {"message1": "invalid inputs"})
    return render(request, "cahngefarmespassword.html", {"message1": "adhar number is not available"})


def fquery(request):
    res = request.session.get("adharno")
    if res:
        return render(request, "fquery.html")
    else:
        return redirect("agriculturelogin")



def savequery(request):
      name=request.POST["t1"]
      email=request.POST["t2"]
      query=request.POST["t3"]
      Query(name=name,email=email,query=query).save()
      ss=messages.success(request,"send query successfully")
      return redirect('fquery')


def farmesvideo(request):
    res = request.session.get("adharno")
    if res:
        all = uplaodvideomodel.objects.all()
        return render(request, "viwtechnology.html", {"data": all})
    else:
        return redirect("agriculturelogin")



def fsoilinformation(request):
    res = request.session.get("adharno")
    if res:
        all = soilinformation.objects.all()
        return render(request, "farmersviewsoilinfo.html", {"data": all})
    else:
        return redirect("agriculturelogin")



def fcropinformation(request):
    res = request.session.get("adharno")
    if res:
        all = cropinformation.objects.all()
        return render(request, "fcropinfo.html", {"data": all})
    else:
        return redirect("agriculturelogin")



def studentslogin(request):
    return render(request,"studentslogin.html")
def openstudent(request):
    return render(request,"stdudentswelcome.html")

def studwelcome(request):
    try:
        name = request.POST["t1"]
        pas = request.POST["t2"]
        all = StudentsModel.objects.get(name=name, password=pas)
        request.session["email"] = all.email
        return redirect("openstudent")
    except StudentsModel.DoesNotExist:
      message="please enter the correct username and password"
      return render(request, "studentslogin.html",{"message":message})

def studentsregistration(request):
    return render(request,"studenstsregistration.html")


def savestudents(request):
    try:
        name = request.POST["t1"]
        passw = request.POST["t2"]
        email = request.POST["t3"]
        univer = request.POST["t4"]
        qual = request.POST["t5"]
        add = request.POST["t6"]
        messages.success(request, "successfully Registration ")
        StudentsModel(name=name,password=passw,email=email,universityname=univer,qualification=qual,address=add).save()
        return redirect('studentregi')
    except IntegrityError:
        messages.success(request,"This email id already available")
        return redirect('studentregi')


def studentsforget(request):
    return render(request,"studentsconform.html")


def studentsconf(request):
    name=request.POST["t1"]
    email=request.POST["t2"]
    all=StudentsModel.objects.all()
    for x in all:
        if name==x.name and email==x.email:
            return render(request,"studentsconformation.html")
    return render(request,"studentsconform.html",{"message":"This email_id is not available"})


def studpasschange(request):
    name=request.POST["t1"]
    email=request.POST["t2"]
    passw=request.POST["t3"]
    con=request.POST["t4"]
    all=StudentsModel.objects.all()
    for x in all:
        if name == x.name and email == x.email and passw == con:
            res = StudentsModel.objects.filter(email=email)
            res.update(password=passw)
            return render(request, "studentsconformation.html", {"message": "changed successfully"})
        else:
            return render(request, "studentsconformation.html", {"message1": "invalid inputs"})
    return render(request, "studentsconformation.html", {"message1": "email id is not available"})


def stdsoilinformation(request):
    res = request.session.get("email")
    if res:
        all = soilinformation.objects.all()
        return render(request, "stdsoilinfo.html", {"data": all})
    else:
        return redirect("studentslog")



def studcropinfo(request):
    res = request.session.get("email")
    if res:
        return render(request, "studcropinf.html")
    else:
        return redirect("studentslog")


def search(request):
    res = request.session.get("email")
    if res:
        try:
            name = request.POST["t1"]
            all = cropinformation.objects.get(name=name)
            return render(request, "studcropinf.html", {"data": all})
        except cropinformation.DoesNotExist:
            return render(request, "studcropinf.html", {"message": name})
    else:
        return redirect("studentslog")




def goodsprice(request):
    res = request.session.get("email")
    if res:
        return render(request, "goods.html")
    else:
        return redirect("studentslog")



def goodpricenamewise(request):
    try:
        name = request.POST["t1"]
        all = goodspricemodule.objects.get(goodsname=name)
        return render(request, "goodpricenamewise.html", {"data": all})
    except goodspricemodule.DoesNotExist:
        return render(request, "goodpricenamewise.html", {"data1":"please enter correct name"})

def stdviewsgoods(request):
    all=goodspricemodule.objects.all()
    return render(request,"studentsviewallgoods.html",{"data":all})

def studentsquery(request):
    return render(request,"stdquey.html")


def savestdqury(request):
    name=request.POST["t1"]
    email=request.POST["t2"]
    uni=request.POST["t3"]
    query=request.POST["t4"]
    studentsQuery(name=name,email=email,universityname=uni,query=query).save()
    return render(request,"stdquey.html",{"message":"query send successfully"})


def weather(request):
    return render(request,"weather.html")


def weather1(request):
    import requests
    try:
        api_add = 'http://api.openweathermap.org/data/2.5/weather?appid=3e60c8d02117eb798b17e88aa52dc803&q='
        city = request.POST["t1"]
        url = api_add + city
        json_data = requests.get(url).json()
        print(json_data)
        ss = json_data['weather'][0]['main']
        kk = json_data['coord']['lon']
        des = json_data['weather'][0]['description']
        temp = json_data['main']['temp']
        temp_min = json_data['main']['temp_min']
        temp_max = json_data['main']['temp_max']
        pressure = json_data['main']['pressure']
        humi = json_data['main']['humidity']
        speed = json_data['wind']['speed']
        print(speed)
        ww=temp-273.15
        return render(request, "showweather.html",
                      {"weather": ss, "loc": kk, "city": city, "temp":ww, "temp_min": temp_min, "temp_max": temp_max,
                       "pressure": pressure, "humidity": humi, "des": des,"wind":speed})
    except:
        return render(request,"weather.html",{"messages":"invalid city_name"})


def adminviewquery(request):
    res = request.session.get("email")
    if res:
        return render(request, "viewquery.html")
    else:
        return redirect("adminlogin")


def viewstdquery(request):
    all=studentsQuery.objects.all()
    return render(request,"viewstudentsquery.html",{"data":all})


def stdreply(request):
    name=request.POST["t1"]
    email=request.POST["t2"]
    data=studentsQuery.objects.get(email=email)
    return render(request,"replay.html",{"data":data})


def sendquery(request):
    name=request.POST["t1"]
    email=request.POST["t2"]
    query=request.POST["t3"]
    ans=request.POST["t4"]
    ss=studentsQuery.objects.all()
    sub = " this efarmers wesite "
    mess = ans
    send_mail(sub, mess, se.EMAIL_HOST_USER, [email])
    return render(request,"viewstudentsquery.html",{"message":"send","data":ss})


def farmesquery(request):
    all=Query.objects.all()
    return render(request,"farmersquery.html",{"data":all})


def farmersreply(request):
    email = request.POST["t2"]
    data = Query.objects.get(email=email)
    return render(request,"farmesreply.html",{"data": data})


def querysend(request):
    name = request.POST["t1"]
    email = request.POST["t2"]
    query = request.POST["t3"]
    ans = request.POST["t4"]
    ss = Query.objects.all()
    sub = " this efarmers wesite "
    mess = ans
    send_mail(sub, mess, se.EMAIL_HOST_USER, [email])
    return render(request, "farmersquery.html", {"message": "send", "data": ss})


def officerquerysave(request):
    name=request.POST["t1"]
    email=request.POST["t2"]
    query=request.POST["t3"]
    oficersquerymodel(name=name,email=email,query=query).save()
    return render(request,"viewquery.html",{"data":" successfully send query to officers"})


def officerqueryview(request):
    res = request.session.get("email")
    if res:
        all = oficersquerymodel.objects.all()
        return render(request, "viewallofficersquery.html", {"data": all})
    else:
        return redirect("agriculturelogin")




def offreply(request):
    name=request.POST["t1"]
    email=request.POST["t2"]
    query=request.POST["t3"]
    data=oficersquerymodel.objects.get(email=email)
    return render(request,"officersrely.html",{"data":data})


def sendans(request):
    name = request.POST["t1"]
    email = request.POST["t2"]
    query = request.POST["t3"]
    ans = request.POST["t4"]
    ss = oficersquerymodel.objects.all()
    sub = " this efarmers wesite "
    mess = ans
    send_mail(sub, mess, se.EMAIL_HOST_USER, [email])
    return render(request, "viewallofficersquery.html", {"message": "send", "data": ss})


def adminlogout(request):
    del request.session["email"]
    return redirect('adminlogin')


def officerlogout(request):
    del request.session["email"]
    return redirect('agriculturelogin')

def farmerlogout(request):
    del request.session["adharno"]
    return redirect('farmerslogin')


def studentslogout(request):
    del request.session["email"]
    return redirect('studentslog')