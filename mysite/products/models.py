from django.db import models
from django.utils import timezone
from accounts.models import User
from django.urls import reverse
from extensions.utils import jalali_converter

# Create your models here.
class ProductsCategory(models.Model):
    parent=models.ForeignKey('self',null=True,blank=True,related_name="child",on_delete=models.SET_NULL)
    title=models.CharField(null=True,max_length=30)
    slug=models.SlugField(null=True)
    is_visible=models.BooleanField(default=True)
    position=models.IntegerField(null=True)
    class Meta:
        ordering = ('position',)
        verbose_name = 'دسته بندی کالا'
        verbose_name_plural = 'دسته بندی های کالا '

    def __str__(self):
        return self.title
    
class Product(models.Model):
    
    COLOR_CHOICES=(('white','سفید'),('yellow','زرد'),('orange','نارنجی'),('red','قرمز'),
                   ('pink','صورتی'),('purple','بنفش'),('blue','آبی'),('green','سبز'),('brown','قهوه ای'),
                   ('black','مشکی'),('gray','طوسی'),('golden','طلایی'),('silver','نقره ای'),)

    USERSTATUS_CHOICES=(('demander','تقاضا کننده'),('supplier','رضه کننده'))
    
    userstatus=models.CharField(choices=USERSTATUS_CHOICES,default='demander',max_length=50)
    
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_products',null=True,verbose_name='نام کاربری')
    
    category=models.ManyToManyField('ProductsCategory',blank=True,verbose_name='دسته بندی کالا')
    
    title=models.CharField(null=True,max_length=30,verbose_name='نام کالا')
    thumbnail=models.ImageField(upload_to='image',null=True,blank=True,verbose_name='تصویر')
    slug=models.SlugField(null=True,allow_unicode=True)
    consumed=models.CharField(null=True,max_length=8000,verbose_name='مورد مصرف')
    description=models.TextField(null=True,verbose_name='معرفی کالا')
    constituents=models.CharField(null=True,max_length=8000,verbose_name='اهم اجزای تشکیل دهنده')
    analytical_material=models.CharField(null=True,max_length=8000,verbose_name='مواد آنالیز')
    #dimensions=models.
    color=models.CharField(choices=COLOR_CHOICES,null=True,max_length=50,verbose_name='رنگ',blank=True)
    count=models.IntegerField(null=True,verbose_name='تعداد',blank=True)
    capacity=models.CharField(null=True,verbose_name='ظرفیت',blank=True,max_length=50,)
    created=models.DateTimeField(auto_now_add=timezone.now,null=True)
    updated=models.DateTimeField(auto_now=timezone.now,)
    price=models.DecimalField(max_digits=6, decimal_places=2,verbose_name='قیمت',null=True)
    manufacturers=models.CharField(max_length=5000,verbose_name='تولیدکنندگان',null=True)
    
    
    class Meta:
       verbose_name = 'کالا'
       verbose_name_plural = 'کالا ها'
      #ordering=('-publish',)
    def __str__(self):
       return self.title
    def get_category(self):
        return ', '.join([cat.title for cat in self.category.all()])
    def get_categoryslug(self):
        return ', '.join([cat.slug for cat in self.category.all()])
    
   # def get_absolute_url(self):
      #  return reverse("blog:post_detail" , kwargs={"year":self.publish.year,"month":self.publish.month,"day":self.publish.day,"slug":self.slug})
    #def save(self, *args, **kwargs):
        slug = ""
        for char in self.title:
            if char.isalpha():
                slug += char
            elif char == " ":
                slug += "-"
        self.slug = slug
        super().save(*args, **kwargs)
#def save error dare bARAYE POST_DETAIL
