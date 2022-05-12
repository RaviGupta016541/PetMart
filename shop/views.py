import datetime
from mimetypes import add_type
from string import whitespace
from tkinter.messagebox import Message
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Adds
from math import ceil
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth  import authenticate,  login, logout


# Create your views here.
"""
def index(request):
    ads= Adds.objects.all()
    n= len(ads) 
    nSlides= n//4 + ceil((n/4) -(n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'ads': ads}
    return render(request,"shop/index1.html", params)

"""
def index(request):
    
    allAds = []
    categoryAdds = Adds.objects.values('petCatgory', 'id','adType')
    print(categoryAdds)
    cats = {item['petCatgory'] for item in categoryAdds}
    for cat in cats:
        ad = Adds.objects.filter(petCatgory=cat).exclude(adType='Lost Pets Ad')
        n = len(ad)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allAds.append([ad, range(1, nSlides), nSlides])
    params = {'allAds':allAds}
    print(params)
    return render(request, 'shop/index.html', params)

def search(request):
    ads= Adds.objects.all()
    if request.method=="GET":
        st=request.GET.get('search')
        if st!=None:
            ads= Adds.objects.filter(addName__icontains=st,petCatgory__icontains=st) 
    print(ads)
    params={"searchAdd":ads}
    print(params)
    return render(request, 'shop/search.html', params)

def about(request):
    return HttpResponse("this is about")
def contact(request):
    return HttpResponse("this is contact")


# to view a specific ads
def adview(request,adid):
    #return HttpResponse("this is addpview")
    ad = Adds.objects.filter(id=adid)
    ad2 = Adds.objects.filter(id=adid)\
            .values_list('userId', flat=True)
    
    print("----")
    #my_values = [item.userId for item in ad]
    print(ad2[0])
    idOfUser=Adds.userId
    print(idOfUser)
    userdetails=User.objects.filter(id=ad2[0])
    print(userdetails)
    params = {'Ad':ad[0],'User':userdetails[0]}
    print("params ke anddar hai",params,params['Ad'])
    return render(request, 'shop/adview.html',params)

def handleSignUp(request):
    if request.method=="POST":
       
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        
        # check for errorneous input
        if len(username)<10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('/')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('/')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('/')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        # myuser.mobile_number=pno
        myuser.save()
        
        messages.success(request, " Your account has been successfully created")
        return redirect('/')

    else:
        return HttpResponse("404 - Not found")

def addAd(request):
    
        # if user is not None:
        #     login(request, user)
        #     messages.success(request, "Successfully Logged In")
        #     return redirect('/')
        # else:
        #     messages.error(request, "Invalid credentials! Please try again")
        #     return redirect('/')

    #return HttpResponse("404- Not found")
    if request.user.is_authenticated:
        return render(request, 'shop/addAd.html')
    else:
        messages.error(request, "First you need to login than you can post a Ad")
        return redirect('/')
    

def saveAds(request):
    if request.method=="POST":
        adType=request.POST.get('ChooseAd')
        addName=request.POST.get('addName')
        petCatgory=request.POST.get('petCatgory')
        addDescription=request.POST.get('addDescription')
        userId=request.user.id
        pno=request.POST.get('pno')
        state=request.POST.get('state')
        city=request.POST.get('city')
        price=request.POST.get('price')
        pub_date=datetime.datetime.now().date()
        image=request.FILES['img']
        if price=='':
            price=0
        data=Adds(adType=adType,addName=addName,userId=userId,pub_date=pub_date,petCatgory=petCatgory,
                  addDescription =addDescription,state=state,city=city,price=price,image=image,pno=pno)
        data.save()
        messages.success(request, "Your Ad has been successfully created")
    return render(request, 'shop/addAd.html')

def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('/')
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect('/')

    return HttpResponse("404- Not found")

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')

def Adoption(request):
    PetAdoptionAdd = Adds.objects.filter(adType="Pet Adoption")
    print(PetAdoptionAdd)
    params={'adoption':PetAdoptionAdd}
    print(params)
    return render(request, 'shop/AdoptionAd.html', params)

def lostPet(request):
    lostPetAdd = Adds.objects.filter(adType="Lost Pets Ad")
    print(lostPetAdd)
    params={'lostPet':lostPetAdd}
    print(params)
    return render(request, 'shop/lostPet.html', params)

