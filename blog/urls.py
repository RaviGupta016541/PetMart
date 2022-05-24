from . import views
from django.urls import path
urlpatterns = [
    path("",views.blogHome,name="blogHome"),
    path('<str:slug>',views.blogPost,name='blogPost'),
    path('add/addBlog',views.addBlog,name='addBlog'),
    path('add/saveBlog',views.saveBlog,name='saveBlog'),
    
]