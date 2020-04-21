from django.db import models
class admin(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=10)
class otp(models.Model):
    otp1=models.IntegerField()
class agricultureofficers(models.Model):
    idno=models.IntegerField(unique=True)
    name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=20)
    profession=models.CharField(max_length=40)
    expertise=models.CharField(max_length=20)
class schememodel(models.Model):
      schemename=models.CharField(max_length=200)
      schemedes=models.CharField(max_length=3000)
class goodspricemodule(models.Model):
      goodsname=models.CharField(max_length=50,unique=True)
      goodsprice=models.FloatField()
      goodsquantity=models.CharField(max_length=10)
      category=models.CharField(max_length=30)
      goodsphoto=models.ImageField(upload_to='goods/')
class uplaodvideomodel(models.Model):
    name=models.CharField(max_length=50)
    video=models.ImageField(upload_to='goods/')
    description=models.CharField(max_length=1000)
class soilinformation(models.Model):
    name=models.CharField(max_length=30,unique=True)
    state=models.CharField(max_length=1000)
    rich=models.CharField(max_length=1000)
    lacks=models.CharField(max_length=1000)
    crops=models.CharField(max_length=1000)
    simage=models.ImageField(upload_to='soilimages/')
class cropinformation(models.Model):
    name=models.CharField(unique=True,max_length=30)
    croptype=models.CharField(max_length=50)
    cropverities=models.CharField(max_length=1000)
    temp=models.CharField(max_length=50)
    rain=models.CharField(max_length=50)
    soiltype=models.CharField(max_length=50)
    highpro=models.CharField(max_length=1000)
    majorpro=models.CharField(max_length=1000)
    highprocountry=models.CharField(max_length=100)
    cropimage=models.ImageField(upload_to='cropimages/')
class farmersmodel(models.Model):
    name=models.CharField(max_length=30)
    password=models.CharField(max_length=10)
    adharno=models.IntegerField(unique=True)
class Query(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    query=models.CharField(max_length=100)
class StudentsModel(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=30)
    universityname=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    qualification=models.CharField(max_length=30)
class studentsQuery(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    query = models.CharField(max_length=100)
    universityname = models.CharField(max_length=100)
class oficersquerymodel(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    query = models.CharField(max_length=100)






