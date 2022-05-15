
from . import views
from django.urls import path

urlpatterns = [
    path("",views.index,name="homePage"),
    path("about/",views.about,name="aboutus"),
    path("search/",views.search,name="search"),
    path("contact/",views.contact,name="contact"),
    path("adview/<int:adid>",views.adview,name="adview"),
    path('signup/', views.handleSignUp, name="handleSignUp"),
    path('login/', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    path('addAd', views.addAd, name="addAd"),
    path('saveAds', views.saveAds, name="saveAds"),
    path('Adoption', views.Adoption, name="Adoption"),
    path('lostPet', views.lostPet, name="lostPet"),
]

 