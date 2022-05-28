import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Adds, Contact
from math import ceil
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth  import authenticate,  login, logout

# for home page
def index(request):
    allAds = []
    categoryAdds = Adds.objects.values('petCatgory', 'id','adType')
    cats = {item['petCatgory'] for item in categoryAdds}
    for cat in cats:
        ad = Adds.objects.filter(petCatgory=cat).exclude(adType='Lost Pets Ad').exclude(adType='Pet Food/Accessories Ad')
        n = len(ad)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allAds.append([ad, range(1, nSlides), nSlides])
    params = {'allAds':allAds}
    return render(request, 'shop/index.html', params)

#for extact data related to given data
def search(request):
    ads= Adds.objects.all()
    if request.method=="GET":
        st=request.GET.get('search')
        if st!=None:
            ads= Adds.objects.filter(addName__icontains=st,petCatgory__icontains=st) 
    params={"searchAdd":ads}
    return render(request, 'shop/search.html', params)

# for contact page data store to database
def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "shop/contactUs.html")
    
# to view a specific ads
def adview(request,adid):
    ad = Adds.objects.filter(id=adid)
    ad2 = Adds.objects.filter(id=adid)\
            .values_list('userId', flat=True)
    
    userdetails=User.objects.filter(id=ad2[0])
    params = {'Ad':ad[0],'User':userdetails[0]}
    return render(request, 'shop/adview.html',params)

# to handle signup details
def handleSignUp(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        
        # check for errorneous input
        if len(username)<5 or len(username)>15:
            messages.error(request, " Your user name must be under 5 to 15 characters")
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
        myuser.save()
        messages.success(request, " Your account has been successfully created")
        return redirect('/')
    else:
        return HttpResponse("404 - Not found")
    
# add Ads page
def addAd(request):
    if request.user.is_authenticated:
        return render(request, 'shop/addAd.html')
    else:
        messages.error(request, "First you need to login than you can post a Ad")
        return redirect('/')
    
# save a Ad 
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

# to handle login details
def handeLogin(request):
    if request.method=="POST":
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

# to handle logout details
def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')

#for adoption pets Ads 
def Adoption(request):
    PetAdoptionAdd = Adds.objects.filter(adType="Pet Adoption")
    params={'adoption':PetAdoptionAdd}
    return render(request, 'shop/AdoptionAd.html', params)

#for lost pets Ads
def lostPet(request):
    lostPetAdd = Adds.objects.filter(adType="Lost Pets Ad")
    params={'lostPet':lostPetAdd}
    return render(request, 'shop/lostPet.html', params)

#for accessories Ads
def accessoriesAd(request):
    accessoriesAd = Adds.objects.filter(adType="Pet Food/Accessories Ad")
    params={'lostPet':accessoriesAd}
    return render(request, 'shop/accessoriesAd.html', params)

