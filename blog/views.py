
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from blog.models import Post

# Create your views here.
def blogHome(request):
    #return HttpResponse("done")
    allPosts= Post.objects.all()
    context={'allPosts': allPosts}
    return render(request, "home.htm", context)
    #return render(request, "blog/blogHome.html", context)
    #return render(request,"")
def blogPost(request, slug):
    post=Post.objects.filter(slug=slug).first()
    context={"post":post}
    return render(request,"blogPost.html",context)
# def addBlog(request):
#     return render(request,"addBlog.html")
def addBlog(request):
    if request.user.is_authenticated:
        return render(request, 'addBlog.html')
    else:
        messages.error(request, "First you need to login than you can post a blog")
        return redirect('/')
def saveBlog(request):
    if request.method=="POST":
        title=request.POST.get('blogName')
        content=request.POST.get('content')
        firstname=request.user.first_name
        lastname=request.user.last_name
        author=firstname+' '+lastname
        
        #pub_date=datetime.datetime.now().date()
        image=request.FILES['img']
        data=Post(title=title,author=author,content=content,image=image)
        data.save()
        messages.success(request, "Your Blog has been successfully created")
    return render(request,'addBlog.html')
