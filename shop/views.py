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
    categoryAdds = Adds.objects.values('petCatgory', 'id')
    print(categoryAdds)
    cats = {item['petCatgory'] for item in categoryAdds}
    for cat in cats:
        ad = Adds.objects.filter(petCatgory=cat)
        n = len(ad)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allAds.append([ad, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    
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
def addpost(request):
    return HttpResponse("this is addpost")

# to view a specific ads
def adview(request,adid):
    #return HttpResponse("this is addpview")
    ad = Adds.objects.filter(id=adid)
    params = {'Ad':ad[0]}
    return render(request, 'shop/adview.html',params)

def handleSignUp(request):
    if request.method=="POST":
        print("inside handle bro 11 ")
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        pno=request.POST['pno']
        state=request.POST['state']
        city=request.POST['city']
        # check for errorneous input
        if len(username)<10:
            messages.danger(request, " Your user name must be under 10 characters")
            return redirect('/')

        if not username.isalnum():
            messages.danger(request, " User name should only contain letters and numbers")
            return redirect('/')
        if (pass1!= pass2):
             messages.danger(request, " Passwords do not match")
             return redirect('/')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.PhoneNo=pno
        myuser.save()
        print("inside handle bro 22")
        messages.success(request, " Your account has been successfully created")
        return redirect('/')

    else:
        return HttpResponse("404 - Not found")

def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')