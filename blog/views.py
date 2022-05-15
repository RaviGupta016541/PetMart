from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def blogHome(request):
    #return HttpResponse("done")
    
    return render(request,"home.htm")
def blogPost(request, slug):
    #return HttpResponse("done")
    return HttpResponse(f"this is blog post:{slug}")