from typing import Iterable
from django.db import models
from django.utils import timezone
from accounts.models import User
from django.urls import reverse
from extensions import utils
from extensions.utils import jalali_converter
from products.models import Product
from services.models import Services
from taggit.managers import TaggableManager
# Create your models here.


class Post(models.Model):
    TYPE_CHOICES=(('product','کالا'),('service','خدمات'))
    type=models.CharField(choices=TYPE_CHOICES,default='product',max_length=30)
    product=models.ForeignKey(Product,related_name='blog_productpost',on_delete=models.CASCADE,blank=True,null=True)
    service=models.ForeignKey(Services,related_name='blog_servicepost',on_delete=models.CASCADE,blank=True,null=True)
    created=models.DateTimeField(auto_now_add=timezone.now,null=True)
    updated=models.DateTimeField(auto_now=timezone.now,)
    slug=models.CharField(null=True,blank=True,max_length=500)
    category=models.CharField(null=True,blank=True,max_length=500)
    tags=TaggableManager()
    class Meta:
      verbose_name = 'آگهی'
      verbose_name_plural = 'آگهی ها'
    
    
    def save(self,*args,**kwargs) :
        if not self.slug:
            if self.type=='product':
                self.slug=self.product.slug
                self.category=self.product.get_categoryslug()
            else:
                self.slug=self.service.slug
                self.category=self.service.get_categoryslug()
        return super().save(*args,**kwargs)
    
 

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='postcomments',null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_postcomment',null=True,verbose_name='نام کاربری')
    percentage=models.DecimalField(verbose_name='درصد',decimal_places=2,null=True,max_digits=6)
    title=models.CharField(verbose_name='عنوان نظر *',null=True,max_length=5000)
    pos=models.CharField(verbose_name='نکات مثبت',null=True,blank=True,max_length=5000)
    neg=models.CharField(verbose_name='نکات منفی',null=True,blank=True,max_length=5000)
    body=models.TextField(verbose_name='متن نظر *',null=True)
    thumbnail=models.ImageField(upload_to='image',null=True,blank=True,verbose_name='تصویر')
    active=models.BooleanField(default=True)
    created_on=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['-created_on']
        verbose_name='نظر'
        verbose_name_plural = 'نظر ها'
    def __str__(self):
        return 'ProductComment {} by {} '.format(self.body,self.title)
    def jcreated_on(self):
        return(jalali_converter(self.created_on))





