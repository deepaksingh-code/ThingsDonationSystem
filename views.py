from django.shortcuts import render
from django.http import HttpResponseRedirect
from app.models import Donator,Address,Pincode,Orphanage,Thing
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'home.html')
def loginUser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username, password=password)
        if user is not None:
            print('login')
            login(request, user)
            try:
                d=request.user.donator
                request.session['usertype']='donator'
                print('login as Donator')
            except:
                try:
                    o=request.user.orphanage
                    # o=Orphanage.objects.get(email=request.user.email)
                    request.session['usertype']='orphanage'
                    print('login as Orphanage')
                except:
                    request.session['usertype']='superuser'
                    print("login as Superuser or admin ")
            print(request.session.items())
            return HttpResponseRedirect('/')
        else:
            data='incorroct username or password!!'
            return render(request,'User Login.html',{'data':data})
    else:

        return render(request,'User Login.html')
from datetime import date
def donatorReg(request):
    if request.method=='POST':
        print('post method')
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        name=fname+" "+lname
        print(name)
        email=request.POST.get('email')
        dob=request.POST.get('dob')
        d=date(int(dob[:4]),int(dob[5:7]),int(dob[8:10]))
        mno=request.POST.get('mobileno')
        password=request.POST.get('password')
        username=fname+dob[:4]+lname
        user=User.objects.create_user(username=username,password=password,email=email)
        user.save()
        g=Group.objects.get(name="DonatorsGroup")
        g.user_set.add(user)
        g.save()
        d=Donator(name=name,dob=d,email=email,mobileno=int(mno),user=user)
        d.save()
        return HttpResponseRedirect('login')
    else:
        return render(request,'userRegistration.html')
def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='login')
def thingDonate(request):
    if request.method=='POST':
        name=request.POST.get('name')
        des=request.POST.get('description')
        quantity=request.POST.get('quantity')
        street=request.POST.get('street')
        city=request.POST.get('city')
        dist=request.POST.get('district')
        pin=request.POST.get('pin')
        try:
            pincode=Pincode.objects.get(pincode=int(pin))
        except:
            pincode=Pincode.objects.create(city=city,district=dist,pincode=int(pin))
            pincode.save()
        add=Address.objects.create(streetno=street,pin=pincode)
        add.save()
        d=Donator.objects.get(email=request.user.email)
        orp=request.POST.get('orphanage')
        thing=Thing.objects.create(name=name,description=des,quantity=quantity,address=add,orphanage_id=int(orp),donator=d)
        thing.save()
        # print(request.POST.get('orphanage'))
        return HttpResponseRedirect('/')
    else:
        orp=Orphanage.objects.all()
        return render(request,'thingDonation.html',{'orp':orp})

def orphanageReg(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobileno=request.POST.get('mobileno')
        street = request.POST.get('street')
        city = request.POST.get('city')
        dist = request.POST.get('district')
        pin = request.POST.get('pin')
        username = str(mobileno)
        password = request.POST.get('password')
        try:
            pincode = Pincode.objects.get(pincode=int(pin))
        except:
            pincode = Pincode.objects.create(city=city, district=dist, pincode=int(pin))
            pincode.save()
        address=Address.objects.create(streetno=street+" "+mobileno,pin=pincode)
        address.save()
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        orphanage=Orphanage.objects.create(name=name,address=address,user=user,mobileno=mobileno)
        orphanage.save()
        return HttpResponseRedirect('/')
    else:
        return render(request,'orphanageRegistration.html')
@login_required(login_url='/login')
def profile(request):
    if request.session['usertype']=='donator':
        donator=request.user.donator
        return render(request, 'donatorDashboard.html', {'orphanage':None,'donator':donator})
    elif request.session['usertype']=='orphanage':
        orphanage=request.user.orphanage
        return render(request,'donatorDashboard.html',{'orphanage':orphanage,'donator':None})
    else:
        return HttpResponseRedirect('/admin')
@login_required(login_url='/login')
def approval(request,pk,op):
     t=Thing.objects.get(pk=int(pk))
     if op==1:
        t.objects.update(approval=True)
     else:
        t.objects.update(approval=False)
     return HttpResponseRedirect('/')
