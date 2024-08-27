from django.db import models
from django.utils import timezone
from accounts.models import User
from django.urls import reverse
from extensions.utils import jalali_converter

# Create your models here.
class ProductsCategory(models.Model):
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
    def get_absolute_url(self):
       return reverse("blog:productscategory_list" , kwargs={"category_slug":self.slug})
    
class ProductsSubCategory(models.Model):
    parent=models.ForeignKey(ProductsCategory,blank=True,null=True,on_delete=models.CASCADE)
    title=models.CharField(null=True,max_length=30)
    slug=models.SlugField(null=True)
    is_visible=models.BooleanField(default=True)
    position=models.IntegerField(null=True)
    class Meta:
        ordering = ('position',)
        verbose_name = 'دسته بندی 2 کالا'
        verbose_name_plural = 'دسته بندی های 2 کالا '

    def __str__(self):
        return self.title
    #def get_absolute_url(self):
      # return reverse("blog:productscategory_list" , kwargs={"category_slug":self.slug})

class ProductsSubSubCategory(models.Model):
    parent=models.ForeignKey(ProductsSubCategory,blank=True,null=True,on_delete=models.CASCADE)
    title=models.CharField(null=True,max_length=30)
    slug=models.SlugField(null=True)
    is_visible=models.BooleanField(default=True)
    position=models.IntegerField(null=True)
    class Meta:
        ordering = ('position',)
        verbose_name = 'دسته بندی  3 کالا '
        verbose_name_plural = 'دسته بندی های 3 کالا '

    def __str__(self):
        return self.title
    
class Product(models.Model):
    GRADE_CHOICES=((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'))
    COLOR_CHOICES=(('white','سفید'),('yellow','زرد'),('orange','نارنجی'),('red','قرمز'),
                   ('pink','صورتی'),('purple','بنفش'),('blue','آبی'),('green','سبز'),('brown','قهوه ای'),
                   ('black','مشکی'),('gray','طوسی'),('golden','طلایی'),('silver','نقره ای'),)

    is_seller=models.BooleanField(verbose_name='عرضه کننده / تقاضا کننده',default=True)
    is_legal=models.BooleanField(verbose_name='حقوقی / حقیقی',default=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_products',null=True,verbose_name='نام کاربری')
    grade=models.IntegerField(choices=GRADE_CHOICES,default=1)
    certificate=models.ImageField(upload_to='image',null=True,blank=True,verbose_name='گواهینامه ها')
    category=models.ManyToManyField('ProductsCategory',blank=True,verbose_name='دسته بندی کالا')
    subcategory=models.ManyToManyField('ProductsSubCategory',blank=True,verbose_name='دسته بندی ')
    subsubcategory=models.ManyToManyField('ProductsSubSubCategory',blank=True,verbose_name='دسته بندی 2 ')
    title=models.CharField(null=True,max_length=30,verbose_name='نام کالا')
    thumbnail=models.ImageField(upload_to='image',null=True,blank=True,verbose_name='تصویر')
    slug=models.SlugField(null=True,allow_unicode=True)
    consumed=models.CharField(null=True,max_length=8000,verbose_name='مورد مصرف')
    performance=models.TextField(null=True,verbose_name='عملکرد')
    constituents=models.CharField(null=True,max_length=8000,verbose_name='اهم اجزای تشکیل دهنده')
    analytical_material=models.CharField(null=True,max_length=8000,verbose_name='مواد آنالیز')
    #dimensions=models.
    description=models.TextField(null=True,verbose_name='شرح کالا')
    color=models.CharField(choices=COLOR_CHOICES,null=True,max_length=50,verbose_name='رنگ',blank=True)
    count=models.IntegerField(null=True,verbose_name='تعداد',blank=True)
    capacity=models.CharField(null=True,verbose_name='ظرفیت',blank=True,max_length=50,)
    created=models.DateTimeField(auto_now_add=timezone.now,null=True)
    updated=models.DateTimeField(auto_now=timezone.now,)
    purchaseprice=models.DecimalField(max_digits=6, decimal_places=2,verbose_name='قیمت خرید',null=True)
    sellingprice=models.DecimalField(max_digits=6, decimal_places=2,verbose_name='قیمت فروش',null=True)
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
    def get_subcategory(self):
        return ', '.join([cat.title for cat in self.subcategory.all()])
    def get_subcategoryslug(self):
        return ', '.join([cat.slug for cat in self.subcategory.all()])
    def get_subsubcategory(self):
        return ', '.join([cat.title for cat in self.subsubcategory.all()])
    def get_subsubcategoryslug(self):
        return ', '.join([cat.slug for cat in self.subsubcategory.all()])
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
