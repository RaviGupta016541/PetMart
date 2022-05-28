from enum import unique
from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
# Create your models here.
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=50)
    slug=AutoSlugField(populate_from='title',unique=True,null=True,default=None)
    timeStamp=models.DateTimeField(auto_now_add=True)
    content=RichTextField(blank=True,null=True)
    image=models.ImageField(upload_to="blog/images/",default="")

    def __str__(self):
        return self.title + " by " + self.author