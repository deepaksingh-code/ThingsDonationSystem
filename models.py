from django.db import models
from django.contrib.auth.models import User
# Create your models
class Pincode(models.Model):
    city=models.CharField(max_length=200)
    district=models.CharField(max_length=200)
    pincode=models.IntegerField(primary_key=True)
    state=models.CharField(max_length=100)
    def __str__(self):
        return str(self.pincode)
class Address(models.Model):
    streetno=models.CharField(max_length=1024)
    pin=models.ForeignKey(Pincode,on_delete=models.CASCADE)
    def __str__(self):
        return self.streetno+","+str(self.pin.pincode)
    def fullAddress(self):
        ad=self.streetno+', '+self.pin.city+', '+self.pin.district+', '+self.pin.state+', '+str(self.pin.pincode)
        return ad
class Donator(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField()
    mobileno=models.IntegerField()
    email=models.EmailField()
    # image=models.ImageField(upload_to='/donatorImages',default=None,blank=True,null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,default=None)
    def __str__(self):
        return self.name
class Orphanage(models.Model):
    name=models.CharField(max_length=200)
    address=models.ForeignKey(Address,on_delete=models.CASCADE)
    mobileno=models.IntegerField(default=None)
    user=models.OneToOneField(User,on_delete=models.CASCADE,default=None)
    def __str__(self):
        return self.name

class Thing(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=1024)
    quantity=models.CharField(max_length=200)
    time=models.DateTimeField(auto_now_add=True)
    address=models.ForeignKey(Address,on_delete=models.CASCADE)
    orphanage=models.ForeignKey(Orphanage,on_delete=models.CASCADE)
    donator=models.ForeignKey(Donator,on_delete=models.CASCADE)
    timeofReceving=models.DateTimeField(default=None,null=True,blank=True)
    approval=models.BooleanField(default=False,null=True,blank=True)
    def __str__(self):
        return self. name+"<-"+self.donator.name


# class Inviligilator(models.Model):
#     name=models.CharField(max_length=50)
#     mobileno=models.IntegerField()
#     email=models.EmailField()
#     things=models.ManyToManyField(Thing)
#     user=models.OneToOneField(User,on_delete=models.CASCADE)
#     def __str__(self):
#         return self.name
