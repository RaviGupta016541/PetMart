
from django.db import models

# Create your models here.
class Adds(models.Model):
    addId=models.AutoField
    adType=models.CharField(max_length=20,default="")
    addName=models.CharField(max_length=50,default="")
    petCatgory=models.CharField(max_length=50,default="")
    addDescription=models.CharField(max_length=300,default="")
    userId=models.IntegerField()
    pno=models.CharField(max_length=12,default="")
    state=models.CharField(max_length=50,default="")
    city=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    pub_date=models.DateField(auto_now_add=True)
    image=models.ImageField(upload_to="shop/images/",default="")
    
    def __str__(self):
        return self.addName
    
class Contact(models.Model):
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=255)
     phone= models.CharField(max_length=13)
     email= models.CharField(max_length=100)
     content= models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)
     def __str__(self):
          return "Message from " + self.name + ' - ' + self.email